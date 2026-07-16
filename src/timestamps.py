import whisper

model = whisper.load_model("base")

result = model.transcribe(
    "media/temp/audio.wav",
    word_timestamps=True
)

for segment in result["segments"]:
    print(
        f"{segment['start']:.2f} --> {segment['end']:.2f}"
    )
    print(segment["text"])
    print("-" * 50)