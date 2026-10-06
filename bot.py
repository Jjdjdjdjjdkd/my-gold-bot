import os, urllib.request, urllib.parse, json, time
from datetime import datetime

TOKEN = os.getenv("BOT_TOKEN", "8385087813:AAFv6HNuOX4KQD6yOmWkzCCS6kv-GrJmFTw")
CHAT_ID = os.getenv("CHAT_ID", "8107782156")

def send(msg):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = urllib.parse.urlencode({"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"}).encode()
        req = urllib.request.Request(url, data=data)
        urllib.request.urlopen(req, timeout=20).read()
        print("Sent")
    except Exception as e:
        print(e)

def get_gold():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"
        with urllib.request.urlopen(url, timeout=15) as r:
            return float(json.loads(r.read().decode())['price'])
    except:
        return 4145.0

send("🚀 *Pugara Gold Bot LIVE on Render!* 24/7 ON ✅")

while True:
    try:
        price = get_gold()
        now = datetime.now().strftime("%H:%M:%S")
        print(f"Price: {price}")
        msg = f"📊 *GOLD:* `${price:.2f}`\n⏰ {now} PKT\n🤖 Render 24/7 Bot"
        send(msg)
        time.sleep(300)
    except Exception as e:
        print(e)
        time.sleep(10)
