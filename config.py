from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.environ.get("API_ID", "0"))
    API_HASH = os.environ.get("API_HASH", "")
    LOG_ID = int(os.environ.get("LOG_ID", "0"))
    SESSION_STREAM = os.environ.get("SESSION_STREAM", "")

class Database:
    VIDEO_CALL = {}
    RADIO_CALL = {}
    FFMPEG_PROCESSES = {}
