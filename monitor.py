import requests

def web_response():
    try:
        response = requests.get("https://example.com")
        if response.status_code == 200:
            print("działa")
        else:
            print("bład")
    except Exceptation as a:
        print("bład:", a)

web_response()