import pytest
from notify_telegram import send_telegram_message

@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, call, report):
    if report.failed:
            send_telegram_message(
            token="7606649602:AAGojHdS-bePCl9Kp_sZpw2HZXHOS3C5PGw",
            chat_id="@hin52_bot",
            message=f"❌ Test failed: {node.name}\nError: {report.longreprtext}"
        )
