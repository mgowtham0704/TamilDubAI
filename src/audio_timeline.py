from pydub import AudioSegment
import os


def create_timeline_audio(segments, output_file):

    final_audio = AudioSegment.silent(duration=32000)

    for i, segment in enumerate(segments):

        start = int(segment["start"] * 1000)

        audio_path = f"output/segment_{i}.mp3"

        if os.path.exists(audio_path):

            audio = AudioSegment.from_wav(audio_path)

            final_audio = final_audio.overlay(
                audio,
                position=start
            )

    final_audio.export(
        output_file,
        format="mp3"
    )

    print("Timeline Tamil audio created!")