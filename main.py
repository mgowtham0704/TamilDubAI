import logging

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


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def main():
    try:
        logging.info("Starting TamilDubAI...")
        audio_path = TEMP_DIR / "audio.wav"
        final_audio = TEMP_DIR / "final_tamil_audio.mp3"
        input_video = INPUT_DIR / "video.mp4"
        output_video = OUTPUT_DIR / "tamil_dubbed_final.mp4"

        logging.info("Transcribing audio...")
        segments = transcribe_audio(str(audio_path))

        logging.info("Generating Tamil speech...")
        for i, segment in enumerate(segments):
            tamil = translate_to_tamil(segment["text"])

            create_tamil_audio(
                tamil,
                audio_file=str(OUTPUT_DIR / f"segment_{i}.wav")
            )

        logging.info("Creating timeline audio...")
        create_timeline_audio(
            segments,
            str(final_audio)
        )

        logging.info("Merging video...")
        merge_video(
            str(input_video),
            str(final_audio),
            str(output_video)
        )

        logging.info("✅ TamilDubAI completed successfully!")

    except Exception as e:
        logging.exception(f"Pipeline failed: {e}")


if __name__ == "__main__":
    main()  