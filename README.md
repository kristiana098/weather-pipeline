# 🌦️ Automated Weather Pipeline & Poem Generator

An automated data pipeline built in Python that fetches daily weather metrics, stores them in an SQLite database, and uses the Groq API to generate a creative bilingual (English & Danish) weather comparison poem. The output is compiled and published automatically via GitHub Actions.

## 🚀 Features
- **Automated Weather Fetching:** Pulls daily data via the Open-Meteo API for Aalborg, Athens, and Copenhagen.
- **SQLite Data Storage:** Persists historical weather observations locally.
- **AI Poem Generation:** Leverages Groq's high-speed inference engine to write a poetic weather analysis.
- **CI/CD Automation:** Scheduled daily execution using GitHub Actions.

## 🛠️ Tech Stack
- **Language:** Python 3.11+
- **APIs:** Open-Meteo API, Groq API
- **Database:** SQLite
- **Automation:** GitHub Actions

## ⚙️ Setup & Local Usage
1. Clone the repository:
   ```bash
   git clone [https://github.com/kristiana098/weather-pipeline.git](https://github.com/kristiana098/weather-pipeline.git)
   cd weather-pipeline