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
if dub_button:

    if uploaded_file is None:
        st.error("Please upload a video first.")

    else:
        st.success("UI is ready! Processing pipeline will be connected next.")