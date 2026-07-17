from pathlib import Path

# Base project directory
BASE_DIR = Path(__file__).resolve().parent

# Media folders
MEDIA_DIR = BASE_DIR / "media"

INPUT_DIR = MEDIA_DIR / "input"
OUTPUT_DIR = MEDIA_DIR / "output"
TEMP_DIR = MEDIA_DIR / "temp"

# Models
MODELS_DIR = BASE_DIR / "models"
PIPER_DIR = BASE_DIR / "piper"

# Whisper model
WHISPER_MODEL = "base"

# Piper executable
PIPER_EXE = PIPER_DIR / "piper.exe"

# Piper voice model
PIPER_MODEL = MODELS_DIR / "ta_IN-rasa_female-medium.onnx"

# FFmpeg executable
FFMPEG = "ffmpeg"