import requests
import time
import logging
import smtplib

email = ""  # email to get alerts
email_sender = ""  # email of sender
email_password = ""  # acess token 


# conecting with mail
def send_email(subject, text):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_sender, email_password)
    messeage = f"{subject}\n{text}"
    server.sendmail(email_sender, email, messeage)
    server.quit


logging.basicConfig(
    filename="web_log_status.log",
    level=logging.INFO,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
    )


# "http://www.google.com/404"
# is not working web addres to show how the app working
urls = [
    "https://github.com",
    "http://www.google.com/404",
    "https://example.com"
]


def web_status():
    # checking connection with website
    for url in urls:
        try:
            response = requests.get(url)
            status = "working" if response.status_code == 200 else "ERROR"
            if status == "ERROR":
                send_email(
                        "Web status alert",
                        f"Website with url:{url} is not working"
                )
        except Exception as a:
            status = f"ERROR: {a}"
            send_email("Web status alert", status)

        # save history of connection status to web_log_status.log
        logging.info(f"Adres: {url} - Status: {status}")


def main():
    while True:
        web_status()
        print("next status check in 5min")
        time.sleep(300)


if __name__ == "__main__":
    main()
