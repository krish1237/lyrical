from dotenv import load_dotenv
load_dotenv()

import os
DISCORD_TOKEN = os.getenv("DISCORD_LYRICAL_TOKEN")
LYRICAL_KEY = os.getenv("LYRICAL_APP_KEY")

GENIUS_BASE_URL = "https://genius.p.rapidapi.com"
