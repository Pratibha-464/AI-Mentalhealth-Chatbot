from dotenv import load_dotenv
import os

load_dotenv()
os.environ['GOOGLE_API_KEY'] = os.getenv("gemini_key")

MODEL_NAME = 'gemini-2.5-flash'