import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
api_key = os.getenv("API_KEY")

if not app_name:
    print("Error: APP_NAME is missing.")
elif not api_key:
    print("Error: API_KEY is missing.")
else:
    print(f"Application: {app_name}")
    print(f"API_KEY loaded: {bool(api_key)}")
