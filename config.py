from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")
DATA_BASE = os.environ.get("DATA_BASE")