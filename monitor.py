import requests
from datetime import datetime
import time


urls = [
    "https://github.com",
    "https://google.com",
    "https://example.com"
]


def web_status():
    # sprawdzanie połączenia z stoną
    for url in urls:
        try:
            response = requests.get(url)
            status = "działa" if response.status_code == 200 else "bład"
        except Exception as a:
            status = f"bład {a}"

        # zpais stausu stron do pliku web_log_status.txt
        log_status = (
             f"czas: {datetime.now()}, "
             f"adress: {url}, "
             f"status: {status}\n"
        )

        with open("web_log_status.txt", "a") as log_file:
            log_file.write(log_status)


def main():
    while True:
        web_status()
        print("następny check status za 30min")
        time.sleep(1800)


if __name__ == "__main__":
    main()
