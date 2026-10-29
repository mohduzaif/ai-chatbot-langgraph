
import sqlite3
from pathlib import Path

# Project root / database / chatbot.db
PROJECT_ROOT = Path(__file__).resolve().parent
DB_PATH = PROJECT_ROOT / "database" / "chatbot.db"

def clear_database():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    # IMPORTANT: Stop Streamlit and close all database connections first.
    for suffix in ("", "-wal", "-shm"):
        file_path = Path(str(DB_PATH) + suffix)

        if file_path.exists():
            file_path.unlink()
            print(f"Deleted: {file_path.name}")

    # Create a brand-new, empty SQLite database file.
    with sqlite3.connect(DB_PATH) as conn:
        pass

    print("\nDatabase reset successfully!")
    print(f"New empty database: {DB_PATH}")

if __name__ == "__main__":
    clear_database()
