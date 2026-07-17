import logging

import whisper

from config import WHISPER_MODEL

logger = logging.getLogger(__name__)


def transcribe_audio(audio_path):
    """
    Transcribe audio using OpenAI Whisper.
    Returns a list of timestamped segments.
    """
    try:
        logger.info("Loading Whisper model...")
        model = whisper.load_model(WHISPER_MODEL)

        logger.info("Transcribing audio...")
        result = model.transcribe(
            audio_path,
            word_timestamps=True
        )

        logger.info("Transcription completed.")
        return result["segments"]

    except Exception:
        logger.exception("Speech transcription failed.")
        raise