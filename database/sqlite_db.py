
# Import Required Libraries.
from pathlib import Path
import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver


def get_database_connection_obj():
    # Get the directory where sqlite_db.py is located
    BASE_DIR = Path(__file__).resolve().parent

    # Database path
    DATABASE_PATH = BASE_DIR / "chatbot.db"

    # Create database connection
    conn = sqlite3.connect(
        database=DATABASE_PATH,
        check_same_thread=False
    )
    return conn