from flask import Blueprint, request, jsonify
from backend.utils.drive import download_from_drive
from backend.utils.ffmpeg import cut_video
from backend.config import UPLOAD_FOLDER, OUTPUT_FOLDER
import os
import uuid

process_video_bp = Blueprint('process_video', __name__)


@process_video_bp.route("/", methods=["POST"])
def process_video():
    data = request.json
    file_id = data.get("file_id")
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    credentials = data.get("credentials")

    if not file_id or not start_time or not end_time or not credentials:
        return jsonify({"status": "error", "message": "Missing required parameters"}), 400

    try:
        # Descargar video desde Google Drive
        video_path = download_from_drive(file_id, credentials)
        original_name = os.path.splitext(os.path.basename(video_path))[0]

        # Procesar corte del video
        output_name = f"{original_name}_clip.mp4"
        output_path = cut_video(video_path, start_time, end_time, output_name)

        # Limpieza de archivo temporal original
        os.remove(video_path)

        return jsonify({"status": "success", "output_file": os.path.basename(output_path)})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
