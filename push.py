import os
from pushover import Client

import settings


def notification(message, title="Dinner Notify"):
    client = Client(settings.PUSHER_USER_TOKEN, api_token=settings.PUSHER_API_TOKEN)
    client.send_message(message, title=title)
