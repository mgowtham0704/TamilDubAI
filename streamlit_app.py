import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="TamilDubAI",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🎬 TamilDubAI")
st.subheader("AI-Powered Video Dubbing")

st.divider()

# -----------------------------
# Upload Video
# -----------------------------
uploaded_file = st.file_uploader(
    "📤 Upload a Video",
    type=["mp4", "mov", "avi", "mkv"]
)

# -----------------------------
# Language Selection
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "🌍 Source Language",
        ["English"]
    )

with col2:
    target_lang = st.selectbox(
        "🌍 Target Language",
        ["Tamil"]
    )

# -----------------------------
# Voice Selection
# -----------------------------
voice = st.selectbox(
    "🎙 Select Voice",
    ["Female", "Male"]
)

st.divider()

# -----------------------------
# Dub Button
# -----------------------------
dub_button = st.button(
    "🚀 Dub Video",
    use_container_width=True
)

st.divider()

# -----------------------------
# Progress Area
# -----------------------------
progress_bar = st.progress(0)

status = st.empty()

status.info("Waiting for video upload...")

# -----------------------------
# Placeholder Logic
# -----------------------------
from pathlib import Path
from main import dub_video
from config import INPUT_DIR

if dub_button:

    if uploaded_file is None:
        st.error("Please upload a video first.")

    else:

        input_path = INPUT_DIR / uploaded_file.name

        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        status.info("🚀 Starting TamilDubAI...")

        progress_bar.progress(10)

        output_video = dub_video(str(input_path))

        progress_bar.progress(100)

        status.success("✅ Dubbing completed!")

        st.video(output_video)

        with open(output_video, "rb") as file:
            st.download_button(
                "📥 Download Dubbed Video",
                file,
                file_name="tamil_dubbed.mp4",
                mime="video/mp4",
            )