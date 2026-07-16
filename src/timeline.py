from pydub import AudioSegment

# Create 30 seconds of silence
silence = AudioSegment.silent(duration=30000)

# Save it
silence.export("output/timeline.wav", format="wav")

print("30-second silent audio created!")