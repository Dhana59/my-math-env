import os
from openai import OpenAI

# Scaler config
base_url = os.getenv("API_BASE_URL", "http://localhost:8000")
client = OpenAI(base_url=base_url, api_key="not-needed")

def run_test():
    print("Testing Math Env...")
    try:
        client.post(f"{base_url}/reset")
        print("Reset Success!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_test()