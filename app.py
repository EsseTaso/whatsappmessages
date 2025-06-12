import streamlit as st
import os
import json
from datetime import time

st.set_page_config(page_title="WhatsApp Botu", layout="centered")
st.title("📱 WhatsApp Otomasyon Botu (Planlayıcı)")

# === Giriş Alanları ===
st.subheader("1. Mesaj Formatları")
text_message = st.text_area("✍️ Metin Mesajı", placeholder="Merhaba, nasılsınız?")
image_file = st.file_uploader("🖼️ Resim Gönder", type=["jpg", "jpeg", "png"])
video_file = st.file_uploader("🎥 Video Gönder", type=["mp4", "mov"])
audio_file = st.file_uploader("🎵 Ses Gönder", type=["mp3", "wav", "ogg"])

# === Saat Seçici ===
st.subheader("2. Gönderim Zamanı")
selected_time = st.time_input("⏰ Mesajın gönderileceği saat", value=time(10, 0))

# === Planla Butonu ===
st.subheader("3. Gönderimi Planla")
if st.button("💾 Planı Kaydet"):
    os.makedirs("uploads", exist_ok=True)
    media_paths = {}

    if image_file:
        path = os.path.join("uploads", image_file.name)
        with open(path, "wb") as f:
            f.write(image_file.getbuffer())
        media_paths["image"] = path

    if video_file:
        path = os.path.join("uploads", video_file.name)
        with open(path, "wb") as f:
            f.write(video_file.getbuffer())
        media_paths["video"] = path

    if audio_file:
        path = os.path.join("uploads", audio_file.name)
        with open(path, "wb") as f:
            f.write(audio_file.getbuffer())
        media_paths["audio"] = path

    plan = {
        "text": text_message,
        "media": media_paths,
        "schedule": selected_time.strftime("%H:%M")
    }

    with open("plan.json", "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2, ensure_ascii=False)

    st.success("✅ Gönderim planı başarıyla kaydedildi!")
