import sqlite3


def init_db(db_path: str = "weather.db") -> sqlite3.Connection:
    """
    Create the SQLite database and weather table if it doesn't exist.
    """

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT,
            date TEXT,
            temperature REAL,
            precipitation REAL,
            wind REAL,
            UNIQUE(location, date)
        )
    """)

    conn.commit()
    return conn


def store_weather(conn: sqlite3.Connection, weather_data: list[dict]) -> int:
    """
    Insert weather data into the database.
    Skips duplicates (same location + date).
    Returns number of inserted rows.
    """

    cursor = conn.cursor()
    inserted = 0

    sql = """
        INSERT OR IGNORE INTO weather
        (location, date, temperature, precipitation, wind)
        VALUES (?, ?, ?, ?, ?)
    """

    for w in weather_data:
        cursor.execute(sql, (
            w["location"],
            w["date"],
            w["temperature"],
            w["precipitation"],
            w["wind"],
        ))
        inserted += cursor.rowcount

    conn.commit()
    return inserted


if __name__ == "__main__":
    sample = [
        {
            "location": "Aalborg",
            "date": "2026-03-23",
            "temperature": 12,
            "precipitation": 1.2,
            "wind": 15,
        }
    ]

    conn = init_db()
    inserted = store_weather(conn, sample)
    print(f"Inserted {inserted} row(s)")
    conn.close()