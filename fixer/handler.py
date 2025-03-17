from json import loads
from requests import get

BASE_PATH = "https://data.fixer.io/api/latest?access_key="


def get_rates(api_key):
    response = get(BASE_PATH + api_key)
    if response.status_code == 200:
        return loads(response.text)
    return None

