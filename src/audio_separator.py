import logging
import subprocess
from pathlib import Path


def separate_audio(input_audio: str, output_dir: str) -> Path:
    """
    Separates vocals and background music using Demucs.

    Args:
        input_audio: Path to input WAV/MP3 audio.
        output_dir: Folder where Demucs outputs separated stems.

    Returns:
        Path to the folder containing separated stems.
    """

    input_audio = Path(input_audio)
    output_dir = Path(output_dir)

    logging.info("Starting AI audio separation...")

    command = [
        "demucs",
        "--two-stems", "vocals",
        "-o", str(output_dir),
        str(input_audio)
    ]

    subprocess.run(command, check=True)

    result_folder = (
        output_dir /
        "htdemucs" /
        input_audio.stem
    )

    logging.info("Audio separation completed.")

    return result_folder