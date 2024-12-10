import os
import subprocess


def cut_video(input_path, start_time, end_time, output_name, output_folder="temp/outputs"):
    """
    Corta un video en base a los tiempos proporcionados.

    Args:
        input_path (str): Ruta del archivo de entrada.
        start_time (str): Tiempo de inicio en formato HH:MM:SS.
        end_time (str): Tiempo de fin en formato HH:MM:SS.
        output_name (str): Nombre del archivo de salida.
        output_folder (str): Carpeta de destino para guardar el archivo.

    Returns:
        str: Ruta completa del archivo procesado.
    """
    output_path = os.path.join(output_folder, output_name)
    command = [
        "ffmpeg",
        "-i", input_path,
        "-ss", start_time,
        "-to", end_time,
        "-c", "copy",
        output_path
    ]
    subprocess.run(command, check=True)
    return output_path


def fragment_video(input_path, max_duration, output_folder="temp/uploads/fragments"):
    """
    Divide un video en fragmentos de duración máxima.

    Args:
        input_path (str): Ruta del archivo de entrada.
        max_duration (int): Duración máxima de cada fragmento en segundos.
        output_folder (str): Carpeta donde se guardarán los fragmentos.

    Returns:
        str: Carpeta que contiene los fragmentos generados.
    """
    os.makedirs(output_folder, exist_ok=True)
    command = [
        "ffmpeg",
        "-i", input_path,
        "-c", "copy",
        "-f", "segment",
        "-segment_time", str(max_duration),
        os.path.join(output_folder, "fragment_%03d.mp4")
    ]
    subprocess.run(command, check=True)
    return output_folder
