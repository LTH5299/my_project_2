import requests
import os
from typing import Optional

def send_telegram_message(token: str, chat_id: str, message: str) -> Optional[int]:
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        response = requests.post(
            url,
            json={
                "chat_id": chat_id,
                "text": message,
                "parse_mode": "Markdown"
            },
            timeout=5
        )
        return response.status_code
    except Exception as e:
        print(f"Telegram notification failed: {str(e)}")
        return None