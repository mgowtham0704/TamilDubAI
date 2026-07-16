import json
from pydub import AudioSegment
import os


class TimelineBuilder:

    def __init__(self):

        self.json_file = "media/output/translated_transcript.json"
        self.audio_folder = "media/output/audio"
        self.output_file = "media/output/final_tamil_audio.wav"

    def build(self):

        with open(self.json_file, "r", encoding="utf-8") as f:
            transcript = json.load(f)

        # Calculate total duration
        total_duration = transcript[-1]["end"] * 1000

        # Add 1 second extra
        timeline = AudioSegment.silent(duration=int(total_duration + 1000))

        for i, segment in enumerate(transcript):

            filename = os.path.join(
                self.audio_folder,
                f"segment_{i+1}.mp3"
            )

            speech = AudioSegment.from_file(filename)

            start = int(segment["start"] * 1000)

            timeline = timeline.overlay(
                speech,
                position=start
            )

            print(
                f"Placed segment {i+1} at {segment['start']} sec"
            )

        timeline.export(
            self.output_file,
            format="wav"
        )

        print("Timeline created!")


if __name__ == "__main__":

    TimelineBuilder().build()