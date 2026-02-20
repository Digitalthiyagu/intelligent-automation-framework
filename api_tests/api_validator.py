import requests
import time

def check_api(url):
    start = time.time()
    response = requests.get(url)
    duration = time.time() - start

    return {
        "url": url,
        "status_code": response.status_code,
        "response_time": round(duration, 3)
    }