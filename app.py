import streamlit as st
import random
import time
from main_automation_module import run_automation  # Buraya otomasyon kodunun fonksiyonunu koyacağız

st.set_page_config(page_title="WhatsApp Otomasyon Paneli", layout="centered")
st.title("📲 WhatsApp Toplu Mesaj Gönderimi")

st.markdown("Bu uygulama ile unread (okunmamış) kişilere toplu mesaj gönderebilirsin.")

# --- 1. Kullanıcı Girdileri ---
text_message = st.text_area("✉️ Metin Mesajı (İsteğe bağlı)", max_chars=1000)

# --- 2. Video ve Ses Yükleme (Placeholder - henüz işlenmiyor) ---
video_file = st.file_uploader("🎥 Video Yükle (.mp4)", type=["mp4"])
audio_file = st.file_uploader("🎵 Ses Kaydı Yükle (.mp3, .ogg)", type=["mp3", "ogg"])

# --- 3. Gönder Butonu ---
if st.button("🚀 Gönderimi Başlat"):
    if not text_message and not video_file and not audio_file:
        st.warning("Lütfen en az bir mesaj türü girin (metin, video ya da ses).")
    else:
        with st.spinner("WhatsApp Web ile bağlantı kuruluyor ve mesajlar gönderiliyor..."):
            suffixes = [":)", ";)", ":D", "(:", "(;)" ]
            final_message = f"{text_message.strip()} {random.choice(suffixes)}" if text_message else None
            result = run_automation(final_message, video_file, audio_file)
            st.success("🎉 Gönderim tamamlandı!")
            st.code(result, language="text")
