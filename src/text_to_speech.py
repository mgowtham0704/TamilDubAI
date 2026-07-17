import logging
import subprocess
from pathlib import Path

from config import (
    PIPER_EXE,
    PIPER_FEMALE_MODEL,
    PIPER_MALE_MODEL,
)

logger = logging.getLogger(__name__)


def create_tamil_audio(text, audio_file, voice="Female"):
    """
    Generate Tamil speech using Piper TTS.
    """

    try:
        output_path = Path(audio_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if voice == "Male":
            model = PIPER_MALE_MODEL
        else:
            model = PIPER_FEMALE_MODEL

        logger.info(
            f"Generating Tamil speech using {voice} voice..."
        )

        subprocess.run(
            [
                str(PIPER_EXE),
                "--model",
                str(model),
                "--output_file",
                str(output_path),
            ],
            input=text,
            text=True,
            encoding="utf-8",
            check=True,
        )

        logger.info(f"Audio saved to: {output_path}")

    except Exception:
        logger.exception("Piper TTS generation failed.")
        raise