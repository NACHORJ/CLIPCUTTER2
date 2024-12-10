from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2.credentials import Credentials
import os
import uuid


def download_from_drive(file_id, credentials_info, upload_folder="temp/uploads"):
    """
    Descarga un archivo desde Google Drive.

    Args:
        file_id (str): ID del archivo en Google Drive.
        credentials_info (dict): Información de credenciales de OAuth 2.0.
        upload_folder (str): Carpeta de destino para guardar el archivo.

    Returns:
        str: Ruta completa del archivo descargado.
    """
    # Crear credenciales
    creds = Credentials.from_authorized_user_info(credentials_info)

    # Construir el servicio de Google Drive
    drive_service = build('drive', 'v3', credentials=creds)

    # Solicitar el archivo
    request = drive_service.files().get_media(fileId=file_id)
    file_name = f"{uuid.uuid4()}.mp4"
    file_path = os.path.join(upload_folder, file_name)

    # Descargar el archivo
    with open(file_path, "wb") as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()

    return file_path
