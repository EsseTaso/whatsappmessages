import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def run_automation(base_message, media_paths, max_users=100):
    # Chrome Başlatma
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=./User_Data")
    driver = webdriver.Chrome(service=Service(), options=options)
    driver.get("https://web.whatsapp.com")
    input("QR kod okutulduysa ENTER'a bas...")

    def get_unread_chats():
        chat_list = set()
        time.sleep(3)
        elements = driver.find_elements(By.CSS_SELECTOR, 'div[aria-label="Chat list"] div[tabindex]')
        for e in elements:
            try:
                unread = e.find_element(By.XPATH, ".//span[@aria-label='unread message']")
                name = e.find_element(By.XPATH, './/span[@dir="auto"]').text
                chat_list.add(name)
            except:
                continue
        return list(chat_list)

    def scroll_chat_list():
        chat_box = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Chat list"]')
        for _ in range(15):
            driver.execute_script("arguments[0].scrollTop += 300", chat_box)
            time.sleep(0.5)

    def send_message_to_user(name):
        try:
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            search_box.clear()
            search_box.send_keys(name)
            time.sleep(2)
            result = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'//span[contains(@title, "{name}")]'))
            )
            result.click()
            time.sleep(random.uniform(2, 4))

            # Metin mesajı gönder
            if base_message:
                input_box = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
                )
                input_box.send_keys(f"{base_message} {random.choice(['🙂', '😉', '👋'])}")
                input_box.send_keys(Keys.ENTER)
                time.sleep(1)

            # Medya mesajları gönder
            if media_paths:
                attach_btn = driver.find_element(By.XPATH, '//span[@data-icon="clip"]')
                attach_btn.click()
                time.sleep(1)

                if 'image' in media_paths:
                    img_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
                    img_input.send_keys(os.path.abspath(media_paths['image']))
                    time.sleep(3)
                    send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
                    send_btn.click()
                    time.sleep(2)
                elif 'video' in media_paths:
                    vid_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
                    vid_input.send_keys(os.path.abspath(media_paths['video']))
                    time.sleep(3)
                    send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
                    send_btn.click()
                    time.sleep(2)
                elif 'audio' in media_paths:
                    aud_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
                    aud_input.send_keys(os.path.abspath(media_paths['audio']))
                    time.sleep(3)
                    send_btn = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
                    send_btn.click()
                    time.sleep(2)

            print(f"✅ Gönderildi: {name}")

        except Exception as e:
            print(f"❌ Hata oluştu {name}: {e}")

    # Ana işlem
    scroll_chat_list()
    unread_users = get_unread_chats()[:max_users]

    for i, name in enumerate(unread_users):
        send_message_to_user(name)
        time.sleep(random.uniform(3, 7))

        if (i + 1) % 20 == 0:
            print("🔄 Dinlenme süresi (30 saniye)")
            time.sleep(30)

    driver.quit()
    print("🎉 Tüm mesajlar gönderildi.")
