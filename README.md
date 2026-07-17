# 🎬 TamilDubAI

> **AI-powered Video Dubbing for Tamil using OpenAI Whisper, Deep Translator, Piper TTS, and FFmpeg.**

TamilDubAI is an end-to-end AI video dubbing application that automatically converts spoken dialogue from a video into natural-sounding Tamil speech while preserving the original video.

The project extracts audio from a video, transcribes speech, translates the transcript, generates Tamil speech using AI text-to-speech, and merges the new audio back into the original video.

---

## ✨ Features

* 🎥 Upload any supported video
* 🎙 Automatic speech transcription with OpenAI Whisper
* 🌍 Translation to Tamil
* 🗣 High-quality offline Tamil Text-to-Speech using Piper
* 🎞 Merge dubbed audio with the original video using FFmpeg
* ⚡ Timestamp-based dubbing pipeline
* 💻 Runs completely on your local machine
* 🚀 Streamlit web interface (Coming Soon)

---

## 🛠 Tech Stack

* Python 3
* OpenAI Whisper
* Deep Translator
* Piper TTS
* FFmpeg
* MoviePy
* Streamlit (Upcoming)

---

## 📂 Project Structure

```text
TamilDubAI/
│
├── app/
│   ├── transcriber.py
│   ├── translator.py
│   ├── tts.py
│   ├── video.py
│   └── utils.py
│
├── media/
│   ├── input/
│   ├── temp/
│   └── output/
│
├── models/
│
├── requirements.txt
├── main.py
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/mgowtham0704/TamilDubAI.git
cd TamilDubAI
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Usage

Run the application:

```bash
python main.py
```

Follow the prompts to process your input video.

---

## 🔄 Workflow

```text
Video
   │
   ▼
Extract Audio
   │
   ▼
Speech Transcription
   │
   ▼
Translation
   │
   ▼
Tamil Text-to-Speech
   │
   ▼
Merge Audio with Video
   │
   ▼
Dubbed Video
```

---

## 🚀 Roadmap

### ✅ Version 2.0

* Timestamp-based dubbing
* Whisper transcription
* Translation pipeline
* Offline Tamil TTS
* FFmpeg video rendering

### 🔄 Next

* Streamlit Web Application
* Multiple Tamil voices
* Subtitle generation
* Voice selection
* Multi-language support
* Lip-sync integration
* Docker support
* Cloud deployment

---

## 🤝 Contributing

Contributions, ideas, and suggestions are welcome.

If you'd like to contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

## 👨‍💻 Author

**Gowtham M**

If you found this project useful, consider giving it a ⭐ on GitHub.
