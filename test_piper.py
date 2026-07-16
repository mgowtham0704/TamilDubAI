import subprocess

text = "வணக்கம் தமிழ்நாடு"

process = subprocess.run(
    [
        "piper/piper.exe",
        "--model",
        "models/ta_IN-rasa_female-medium.onnx",
        "--output_file",
        "media/output/test_tamil.wav",
    ],
    input=text,
    text=True,
    encoding="utf-8",
)

print("Done!")