import requests
from datetime import datetime
import time
import logging


logging.basicConfig(
    filename="web_log_status.log)",
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
    )



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

        # zpais statusu stron do pliku web_log_status.log
        log_status = (
             f"czas: {datetime.now()}, "
             f"adress: {url}, "
             f"status: {status}\n"
        )

        logging.info(f"Adres: {url} - Status: {status}")

def main():
    while True:
        web_status()
        print("następny check status za 30min")
        time.sleep(120)


if __name__ == "__main__":
    main()
