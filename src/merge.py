import subprocess


def merge_video(video_path, audio_path, output_path):

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-i", audio_path,
        "-map", "0:v",
        "-map", "1:a",
        "-c:v", "copy",
        "-c:a", "aac",
        output_path
    ], check=True)

    print("✅ Tamil dubbed video created!")


if __name__ == "__main__":

    merge_video(
        "media/input/video.mp4",
        "media/temp/final_tamil_audio.mp3",
        "media/output/tamil_dubbed_final.mp4"
    )