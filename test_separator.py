from src.audio_separator import separate_audio

result = separate_audio(
    "media/temp/audio.wav",
    "media/separated"
)

print(result)