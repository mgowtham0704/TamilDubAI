from moviepy import VideoFileClip, AudioFileClip


class VideoMerger:

    def __init__(self):
        self.video = "media/input/video.mp4"
        self.audio = "media/output/final_tamil_audio.wav"
        self.output = "media/output/tamil_dubbed.mp4"

    def merge(self):
        print("Loading video...")
        video = VideoFileClip(self.video)

        print("Loading Tamil audio...")
        audio = AudioFileClip(self.audio)

        # Use the shorter duration
        duration = min(video.duration, audio.duration)

        video = video.subclipped(0, duration)
        audio = audio.subclipped(0, duration)

        print("Merging...")
        final_video = video.with_audio(audio)

        final_video.write_videofile(
            self.output,
            codec="libx264",
            audio_codec="aac"
        )

        print("Done!")
        print(f"Saved as {self.output}")


if __name__ == "__main__":
    VideoMerger().merge()