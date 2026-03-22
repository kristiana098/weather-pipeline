from fetch import fetch_weather
from store_sql import init_db, store_weather
from generate_poem import generate_poem


def main():
    print("=" * 50)
    print(" Weather Pipeline")
    print("=" * 50)

    # Fetch weather 
    print("\n[1/3] Fetching weather data...")
    weather = fetch_weather()

    if not weather:
        print("No weather data fetched.")
        return

    for w in weather:
        print(w)

    # Store in database 
    print("\n[2/3] Storing data in SQLite...")
    conn = init_db()
    inserted = store_weather(conn, weather)
    print(f"Inserted {inserted} new row(s)")

    # Generate poem 
    print("\n[3/3] Generating poem...")
    poem = generate_poem(weather)

    print("\nGenerated poem:\n")
    print(poem)

    conn.close()

    print("\nPipeline complete.")
    print("=" * 50)


if __name__ == "__main__":
    main()