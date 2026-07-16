import whisper
from deep_translator import GoogleTranslator

model = whisper.load_model("base")

result = model.transcribe(
    "output/audio.wav",
    word_timestamps=True
)

translated_segments = []

for segment in result["segments"]:
    tamil = GoogleTranslator(
        source="auto",
        target="ta"
    ).translate(segment["text"])

    translated_segments.append({
        "start": segment["start"],
        "end": segment["end"],
        "english": segment["text"],
        "tamil": tamil
    })

for seg in translated_segments:
    print("="*60)
    print("Start :", seg["start"])
    print("End   :", seg["end"])
    print("English :", seg["english"])
    print("Tamil   :", seg["tamil"])