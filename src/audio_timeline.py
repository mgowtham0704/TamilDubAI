import logging
from pathlib import Path

from pydub import AudioSegment

from config import OUTPUT_DIR

logger = logging.getLogger(__name__)


def create_timeline_audio(segments, output_file):
    """
    Combine individual Tamil speech segments into one timeline audio.
    """

    try:
        final_audio = AudioSegment.silent(duration=32000)

        for i, segment in enumerate(segments):

            start = int(segment["start"] * 1000)

            audio_path = OUTPUT_DIR / f"segment_{i}.wav"

            if audio_path.exists():

                audio = AudioSegment.from_wav(str(audio_path))

                final_audio = final_audio.overlay(
                    audio,
                    position=start
                )

            else:
                logger.warning(f"Missing audio segment: {audio_path.name}")

        final_audio.export(
            str(output_file),
            format="mp3"
        )

        logger.info("Timeline Tamil audio created.")

    except Exception:
        logger.exception("Timeline audio creation failed.")
        raise