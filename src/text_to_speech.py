import logging
import subprocess
from pathlib import Path

from config import PIPER_EXE, PIPER_MODEL

logger = logging.getLogger(__name__)


def create_tamil_audio(text, audio_file):
    """
    Generate Tamil speech using Piper TTS.
    """
    try:
        output_path = Path(audio_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        logger.info("Generating Tamil speech...")

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

        logger.info(f"Audio saved to: {output_path}")

    except Exception:
        logger.exception("Piper TTS generation failed.")
        raise