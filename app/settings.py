import os
from dotenv import load_dotenv

load_dotenv()
SERVICE_ACCOUNT_EMAIL = os.environ.get("SHEET_SERVICE_EMAIL")
GOOGLE_SHEET_PROJECT_ID = os.environ.get("SHEET_PROJECT")
GOOGLE_SHEET_SERVICE_ACCOUNT_KEY_ID = os.environ.get("SHEET_SERVACCT_KEY_ID")
GOOGLE_SHEET_PRIVATE_KEY = os.environ.get("SHEET_PRV_KEY").replace("\\n", "\n")
GOOGLE_SHEET_CLIENT_ID = os.environ.get("SHEET_CLIENT_ID")
GOOGLE_SHEET_ID = os.environ.get("SHEET_ID")
GOOGLE_SHEET_RANGE = os.environ.get("SHEET_RANGE")
PUSHER_API_TOKEN = os.environ.get("PUSH_API_TOKEN")
PUSHER_USER_TOKEN = os.environ.get("PUSH_USER_TOKEN")
