import json
import asyncio
import edge_tts
import os


class TamilTTS:

    def __init__(self):

        self.input_file = "media/output/translated_transcript.json"
        self.output_folder = "media/output/audio"

        os.makedirs(self.output_folder, exist_ok=True)

        # Microsoft Tamil Neural Voice
        self.voice = "ta-IN-ValluvarNeural"

    async def generate(self):

        with open(self.input_file, "r", encoding="utf-8") as f:

            transcript = json.load(f)

        for i, segment in enumerate(transcript):

            filename = os.path.join(
                self.output_folder,
                f"segment_{i+1}.mp3"
            )

            communicate = edge_tts.Communicate(
                segment["tamil"],
                self.voice
            )

            await communicate.save(filename)

            print(f"Created {filename}")


if __name__ == "__main__":

    asyncio.run(
        TamilTTS().generate()
    )