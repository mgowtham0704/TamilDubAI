import logging
import subprocess

from config import FFMPEG

logger = logging.getLogger(__name__)


def extract_audio(video_path, audio_path):
    """
    Extract audio from a video using FFmpeg.
    """

    try:
        logger.info("Extracting audio...")

        subprocess.run(
            [
                FFMPEG,
                "-y",
                "-i", str(video_path),
                "-vn",
                "-acodec", "pcm_s16le",
                "-ar", "16000",
                "-ac", "1",
                str(audio_path),
            ],
            check=True,
        )

        logger.info("Audio extracted successfully.")

    except Exception:
        logger.exception("Audio extraction failed.")
        raise