import pytest
from notify_telegram import send_telegram_message
import os


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, call, report):
    if report.failed:
        telegram_token = os.getenv("TELEGRAM_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        send_telegram_message(
            token=telegram_token,
            chat_id=chat_id,
            message=f"❌ *Test Failed*: `{node.name}`\n``````"
        )
