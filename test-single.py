import requests

if __name__ == "__main__":
    for x in range(50):
        requests.get("http://localhost:5002")