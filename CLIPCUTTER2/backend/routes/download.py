from flask import Blueprint, send_file, jsonify
from backend.config import OUTPUT_FOLDER
import os

download_bp = Blueprint('download', __name__)


@download_bp.route("/<filename>", methods=["GET"])
def download_file(filename):
    try:
        # Convertir OUTPUT_FOLDER a una ruta absoluta (asegura compatibilidad en Windows)
        output_folder_path = os.path.abspath(OUTPUT_FOLDER)
        file_path = os.path.join(output_folder_path, filename)

        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return jsonify({"status": "error", "message": "File not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
