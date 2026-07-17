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
from pathlib import Path

PIPER_FEMALE_MODEL = Path(
    "models/ta_IN-rasa_female-medium.onnx"
)

PIPER_MALE_MODEL = Path(
    "models/ta_IN-Valluvar-medium.onnx"
)

# Default voice
PIPER_MODEL = PIPER_FEMALE_MODEL

# FFmpeg executable
FFMPEG = "ffmpeg"