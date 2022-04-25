import requests


def email_is_ok(email: str) -> bool:
    edomain = email.split("@")[-1]
    url = "https://raw.githubusercontent.com/disposable/disposable-email-domains/master/domains.json"
    response = requests.get(url)
    if edomain in response.json():
        return False
    return True
