from flask import Blueprint, request, jsonify
from backend.utils.drive import download_from_drive
from backend.utils.ffmpeg import fragment_video
from backend.config import UPLOAD_FOLDER
import os

fragment_video_bp = Blueprint('fragment_video', __name__)


@fragment_video_bp.route("/", methods=["POST"])
def fragment_video_route():
    data = request.json
    file_id = data.get("file_id")
    max_duration = data.get("max_duration", 600)
    credentials = data.get("credentials")

    if not file_id or not credentials:
        return jsonify({"status": "error", "message": "Missing required parameters"}), 400

    try:
        # Descargar video desde Google Drive
        video_path = download_from_drive(file_id, credentials)

        # Fragmentar el video
        fragments_folder = fragment_video(video_path, max_duration)

        # Listar los fragmentos generados
        fragments = os.listdir(fragments_folder)
        fragment_paths = [os.path.join(fragments_folder, f) for f in fragments]

        return jsonify({"status": "success", "fragments": fragment_paths})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
