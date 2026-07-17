import logging
import subprocess

from config import FFMPEG

logger = logging.getLogger(__name__)


def merge_video(video_path, audio_path, output_path):
    """
    Merge the original video with the generated Tamil audio.
    """

    try:
        logger.info("Merging video and audio...")

        subprocess.run(
            [
                FFMPEG,
                "-y",
                "-i", str(video_path),
                "-i", str(audio_path),
                "-map", "0:v",
                "-map", "1:a",
                "-c:v", "copy",
                "-c:a", "aac",
                str(output_path),
            ],
            check=True,
        )

        logger.info(f"Dubbed video saved to: {output_path}")

    except Exception:
        logger.exception("Video merging failed.")
        raise