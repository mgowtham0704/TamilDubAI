import logging
import shutil
from pathlib import Path

from config import (
    INPUT_DIR,
    OUTPUT_DIR,
    TEMP_DIR,
)

from src.speech_to_text import transcribe_audio
from src.translator import translate_to_tamil
from src.text_to_speech import create_tamil_audio
from src.audio_timeline import create_timeline_audio
from src.merge import merge_video
from src.extract_audio import extract_audio

APP_VERSION = "1.0.0"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def dub_video(
    input_video_path,
    progress_callback=None,
    voice="Female"
):
    """
    Runs the complete TamilDubAI pipeline.
    Returns the path to the dubbed video.
    """
    def update(message, progress):
        if progress_callback:
            progress_callback(message, progress)

    audio_path = TEMP_DIR / "audio.wav"
    final_audio = TEMP_DIR / "final_tamil_audio.mp3"
    input_video = INPUT_DIR / "video.mp4"
    output_video = OUTPUT_DIR / "tamil_dubbed_final.mp4"

       # Save uploaded video into INPUT_DIR

    source = Path(input_video_path)

    if source.resolve() != input_video.resolve():
        shutil.copy(source, input_video)
        update("📁 Preparing video...", 5)

    logging.info("Extracting audio...")
    update("🎵 Extracting audio...", 15)
    extract_audio(
        str(input_video),
        str(audio_path)
    )

    logging.info("Transcribing audio...")
    update("🎙️ Transcribing speech...", 30)
    segments = transcribe_audio(str(audio_path))
    logging.info("Generating Tamil speech...")
    update("🌍 Translating to Tamil...", 50)

    
    for i, segment in enumerate(segments):

        tamil = translate_to_tamil(segment["text"])

        create_tamil_audio(
            tamil,
            audio_file=str(OUTPUT_DIR / f"segment_{i}.wav"),
            voice=voice
)
    logging.info("Creating timeline audio...")

    update("🧩 Building timeline audio...", 75)

    create_timeline_audio(
        segments,
        str(final_audio)
    )

    logging.info("Merging video...")
    update("🎬 Merging video...", 90)

    merge_video(
        str(input_video),
        str(final_audio),
        str(output_video)
    )
    update("✅ Completed!", 100)

    return str(output_video)


def main():

    try:

        logging.info(f"Starting TamilDubAI v1.0.0...")

        video = INPUT_DIR / "video.mp4"

        output = dub_video(str(video))

        logging.info(f"Completed: {output}")

    except Exception as e:

        logging.exception(e)


if __name__ == "__main__":
    main()