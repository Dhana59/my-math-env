import os
from openai import OpenAI
base_url = os.getenv("API_BASE_URL", "http://localhost:8000")
client = OpenAI(base_url=base_url, api_key="not-needed")

def run_test():
    print("Testing Math Env...")
    try:
        response = client.post(
            f"{base_url}/reset",
            cast_to=dict   
        )
        print("Reset Success!", response)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_test()
