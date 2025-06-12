import streamlit as st
import os
from datetime import datetime, time as dtime
import time
import schedule

# === Sayfa Ayarları ===
st.set_page_config(page_title="WhatsApp Botu", layout="centered")
st.title("📱 WhatsApp Otomasyon Botu")

# === Giriş Alanları ===
st.subheader("1. Mesaj Formatları")

text_message = st.text_area("✍️ Metin Mesajı", placeholder="Merhaba, nasılsınız?")

image_file = st.file_uploader("🖼️ Resim Gönder", type=["jpg", "jpeg", "png"])
video_file = st.file_uploader("🎥 Video Gönder", type=["mp4", "mov"])
audio_file = st.file_uploader("🎵 Ses Gönder", type=["mp3", "wav", "ogg"])

# === Zamanlama Ayarları ===
st.subheader("2. Zamanlama")
scheduled_time = st.time_input("⏰ Başlangıç Saati", value=dtime(10, 0))
run_now = st.checkbox("Hemen gönderimi başlat")

# === Mesajı Gönder Butonu ===
st.subheader("3. Mesajı Gönder")
if st.button("🚀 Gönderimi Planla veya Başlat"):
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

    def job():
        st.success("🚀 Otomasyon başlatılıyor...")
        st.info("🕒 Lütfen birkaç saniye bekleyin. Mesajlar gönderiliyor...")
        # run_automation(text_message, media_paths)
        st.success("✅ Mesaj gönderimi tamamlandı.")

    if run_now:
        job()
    else:
        now = datetime.now().time()
        scheduled_str = scheduled_time.strftime("%H:%M")
        schedule.every().day.at(scheduled_str).do(job)

        st.warning(f"⏳ Gönderim {scheduled_str}'da başlayacak. Uygulamayı açık tutmalısınız!")

        while True:
            schedule.run_pending()
            time.sleep(1)

# === Alt Bilgi ===
st.markdown("---")
st.caption("Otomasyon geliştirme: Esse x ChatGPT")
