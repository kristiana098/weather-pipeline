import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def generate_poem(weather_data):
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    weather_text = "\n".join([
        f"{w['location']}: {w['temperature']}°C, "
        f"{w['precipitation']}mm rain, {w['wind']} km/h wind"
        for w in weather_data
    ])

    prompt = f"""
Write a short poetic comparison of the weather:

{weather_text}

Requirements:
- Compare the cities
- Say where it is nicest to be tomorrow
- Write in English and Danish
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    poem = response.choices[0].message.content

    # Save to HTML
    os.makedirs("docs", exist_ok=True)

    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(f"""
        <html>
        <body>
        <h1>Weather Poem</h1>
        <pre>{poem}</pre>
        </body>
        </html>
        """)

    return poem