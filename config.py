from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MEDIA_DIR = BASE_DIR / "media"

INPUT_DIR = MEDIA_DIR / "input"
OUTPUT_DIR = MEDIA_DIR / "output"
TEMP_DIR = MEDIA_DIR / "temp"

MODELS_DIR = BASE_DIR / "models"
PIPER_DIR = BASE_DIR / "piper"

WHISPER_MODEL = "base"

PIPER_EXE = PIPER_DIR / "piper.exe"

PIPER_FEMALE_MODEL = MODELS_DIR / "ta_IN-rasa_female-medium.onnx"

PIPER_MALE_MODEL = MODELS_DIR / "ta_IN-Valluvar-medium.onnx"

PIPER_MODEL = PIPER_FEMALE_MODEL

FFMPEG = "ffmpeg"