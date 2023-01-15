import os
import requests

from dotenv import load_dotenv
from urllib.parse import urljoin, urlparse

BITLY_API = 'https://api-ssl.bitly.com/v4/'
def shorten_link(link):
    payload = {'long_url': link}
    bitlink_response = requests.post(urljoin(BITLY_API, 'bitlinks'), headers=auth_user, json=payload)
    bitlink_response.raise_for_status()
    bitlink = bitlink_response.json()['id']
    return bitlink

def count_clicks(bitlink):
    payload = {'unit': 'month', 'units': '-1'}
    click_response = requests.get(urljoin(BITLY_API, f'bitlinks/{bitlink}/clicks/summary'), headers=auth_user,
                                  params=payload)
    click_response.raise_for_status()
    user_click = click_response.json()['total_clicks']
    return user_click

def is_bitlink(parsed_url):
    is_bitlink_response = requests.get(urljoin(BITLY_API, f'bitlinks/{parsed_url}'), headers=auth_user)
    return is_bitlink_response.ok


if __name__ == "__main__":
    load_dotenv()
    bitly_token = os.environ['BITLY_TOKEN']
    auth_user = {'Authorization': f'Bearer {bitly_token}'}
    user_url = input('Введите ссылку: ')
    parsed_url = f'{urlparse(user_url).netloc}{urlparse(user_url).path}'

    target = is_bitlink(parsed_url)
    if not target:
        try:
            bitlink = shorten_link(user_url)
            print('Битлинк:', bitlink)
        except requests.exceptions.HTTPError:
            print('Invalid input')
    else:
        try:
            user_click = count_clicks(parsed_url)
            print('По вашей ссылке прошли:', user_click)
        except requests.exceptions.HTTPError:
            print('Invalid input')