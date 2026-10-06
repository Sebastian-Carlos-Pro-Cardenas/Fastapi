import os
from dotenv import load_dotenv

load_dotenv()

APP_TITTLE:str = os.getenv("APP_TITTLE","The blocks of Minecraft")
APP_VERSION:str = os.getenv("APP_VERSION","0.0.1")
APP_DESCRIPTION:str = os.getenv(
    "APP_DESCRIPTION",
    "Guide of the blocks of Minecraft"
)
DATABASE_NAME:str = os.getenv("DATABASE_NAME","db.sqlite3")
DATABASE_URL:str = os.getenv("DATABASE_URL","sqlite:///./db.sqlite3")