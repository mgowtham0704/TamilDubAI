from pathlib import Path

# Base project directory
BASE_DIR = Path(__file__).resolve().parent

# Folders
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
MEDIA_DIR = BASE_DIR / "media"
MODELS_DIR = BASE_DIR / "models"
PIPER_DIR = BASE_DIR / "piper"

# Models
WHISPER_MODEL = "base"

# Piper voice model (update the filename if yours differs)
PIPER_MODEL = PIPER_DIR / "ta_IN-kani-medium.onnx"

# FFmpeg executable (if needed)
FFMPEG = "ffmpeg"