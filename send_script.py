import json
import time
from datetime import datetime
from automation import run_automation

PLAN_FILE = "plan.json"

def read_plan():
    try:
        with open(PLAN_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def main_loop():
    while True:
        plan = read_plan()
        if not plan:
            print("⏳ Plan dosyası bulunamadı.")
            time.sleep(60)
            continue

        now = datetime.now().strftime("%H:%M")
        if plan["schedule"] == now:
            print("🚀 Zaman geldi, mesaj gönderiliyor.")
            run_automation(plan["text"], plan["media"])
            os.remove(PLAN_FILE)
        else:
            print(f"⌛ Bekleniyor... Şu an: {now}, plan: {plan['schedule']}")
        time.sleep(60)

if __name__ == "__main__":
    main_loop()
