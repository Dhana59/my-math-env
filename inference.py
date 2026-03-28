 import os
import requests
base_url = os.getenv("API_BASE_URL", "http://localhost:8000")

def run_test():
    print("Testing Math Env...")
    try:
        response = requests.post(f"{base_url}/reset")

        if response.status_code == 200:
            print("Reset Success!", response.json())
        else:
            print("Failed:", response.text)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_test()
