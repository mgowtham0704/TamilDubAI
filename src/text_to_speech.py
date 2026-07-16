import subprocess
from pathlib import Path


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Piper executable
PIPER_EXE = PROJECT_ROOT / "piper" / "piper.exe"

# Tamil voice model
PIPER_MODEL = PROJECT_ROOT / "models" / "ta_IN-rasa_female-medium.onnx"


def create_tamil_audio(text, audio_file):
    """
    Generate Tamil speech using Piper TTS.
    """

    output_path = Path(audio_file)

    # Create output directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            str(PIPER_EXE),
            "--model",
            str(PIPER_MODEL),
            "--output_file",
            str(output_path),
        ],
        input=text,
        text=True,
        encoding="utf-8",
        check=True,
    )