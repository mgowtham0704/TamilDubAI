from TTS.api import TTS

print("Loading XTTS model...")

tts = TTS(
    "tts_models/multilingual/multi-dataset/xtts_v2",
    gpu=False
)

print("Generating Tamil voice...")

tts.tts_to_file(
    text="வணக்கம், இது தமிழ் செயற்கை நுண்ணறிவு குரல் சோதனை.",
    speaker_wav="speaker.wav",
    language="ta",
    file_path="tamil_test.wav"
)


print("Completed")