from moviepy import VideoFileClip
from pathlib import Path


def extract_audio(video_path: str, output_path: str):
    """
    Extract audio from a video and save it as a WAV file.
    """

    video = VideoFileClip(video_path)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    video.audio.write_audiofile(
        output_path,
        codec="pcm_s16le"
    )

    video.close()

    print(f"Audio saved to: {output_path}")