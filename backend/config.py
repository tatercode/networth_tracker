import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    access_url = os.getenv("ACCESS_URL")
