from src.speech_to_text import transcribe_audio
from src.translator import translate_to_tamil
from src.text_to_speech import create_tamil_audio
from src.audio_timeline import create_timeline_audio
from src.merge import merge_video


segments = transcribe_audio(
    "media/temp/audio.wav"
)


for i, segment in enumerate(segments):

    tamil = translate_to_tamil(
        segment["text"]
    )

    create_tamil_audio(
        tamil,
        audio_file = f"output/segment_{i}.wav"
    )


create_timeline_audio(
    segments,
    "media/temp/final_tamil_audio.mp3"
)
merge_video(
    "media/input/video.mp4",
    "media/temp/final_tamil_audio.mp3",
    "media/output/tamil_dubbed_final.mp4"
)