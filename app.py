import streamlit as st
import os
from automation import run_automation
import random

# === Sayfa Ayarları ===
st.set_page_config(page_title="WhatsApp Botu", layout="centered")
st.title("📱 WhatsApp Otomasyon Botu")

# === Giriş Alanları ===
st.subheader("1. Mesaj Formatları")

image_file = st.file_uploader("🖼️ Resim Gönder", type=["jpg", "jpeg", "png"])
video_file = st.file_uploader("🎥 Video Gönder", type=["mp4", "mov"])
audio_file = st.file_uploader("🎵 Ses Gönder", type=["mp3", "wav", "ogg"])

# === Mesajı Gönder Butonu ===
st.subheader("2. Mesajı Gönder")
if st.button("🚀 Mesajı Gönder"):
    os.makedirs("uploads", exist_ok=True)
    media_paths = {}

    if image_file:
        image_path = os.path.join("uploads", image_file.name)
        with open(image_path, "wb") as f:
            f.write(image_file.getbuffer())
        media_paths['image'] = image_path

    if video_file:
        video_path = os.path.join("uploads", video_file.name)
        with open(video_path, "wb") as f:
            f.write(video_file.getbuffer())
        media_paths['video'] = video_path

    if audio_file:
        audio_path = os.path.join("uploads", audio_file.name)
        with open(audio_path, "wb") as f:
            f.write(audio_file.getbuffer())
        media_paths['audio'] = audio_path

    st.success("🚀 Otomasyon başlatılıyor...")

    # Emoji listesiyle rastgele emoji mesajı oluştur
    emoji_list = ["🙂", "😉", "👋", "😊", "👍"]
    emoji_message = random.choice(emoji_list)
    st.info(f"📨 Gönderilecek emoji: {emoji_message}")

    # Otomasyonu başlat
    run_automation(emoji_message, media_paths)

    st.success("✅ Mesaj gönderimi tamamlandı.")

# === Alt Bilgi ===
st.markdown("---")
st.caption("Otomasyon geliştirme: Esse x ChatGPT")
