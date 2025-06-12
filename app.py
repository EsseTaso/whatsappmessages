import streamlit as st
import os
from datetime import datetime
import time
from automation import run_automation
import random

# === Sayfa Ayarları ===
st.set_page_config(page_title="WhatsApp Botu", layout="centered")
st.title("📱 WhatsApp Otomasyon Botu")

# === Giriş Alanları ===
st.subheader("1. Mesaj Formatları")

text_message = st.text_area("✍️ Metin Mesajı (Yine de her gönderim için rastgeleleşir)", placeholder="Buraya bir şey yazabilirsiniz veya boş bırakabilirsiniz")

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

    # Her gönderim için random metin oluştur
    sample_texts = [
        "Selam, iyi günler!",
        "Merhaba, kolay gelsin!",
        "Size ulaşmak istedim 😊",
        "Bilgilendirme için yazıyorum.",
        "İyi çalışmalar dilerim!",
        "Size kısa bir bilgilendirme iletmek istedim.",
        "Merhaba, müsait olduğunuzda dönüş yaparsanız sevinirim.",
        "Umarım her şey yolundadır!"
    ]
    randomized_text = random.choice(sample_texts)

    st.success("🚀 Otomasyon başlatılıyor...")
    st.info(f"📨 Gönderilecek mesaj: {randomized_text}")
    run_automation(randomized_text, media_paths)
    st.success("✅ Mesaj gönderimi tamamlandı.")

# === Alt Bilgi ===
st.markdown("---")
st.caption("Otomasyon geliştirme: Esse x ChatGPT")
