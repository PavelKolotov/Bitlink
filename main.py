import os
import requests

from dotenv import load_dotenv
from urllib.parse import urljoin, urlparse


BITLY_API = 'https://api-ssl.bitly.com/v4/'


def shorten_link(bitly_token,link):
    payload = {'long_url': link}
    auth_header = {'Authorization': f'Bearer {bitly_token}'}
    bitlink_response = requests.post(
        urljoin(BITLY_API, 'bitlinks'),
        headers=auth_header,
        json=payload
    )
    bitlink_response.raise_for_status()
    bitlink = bitlink_response.json()['link']
    return bitlink


def count_clicks(bitly_token, bitlink):
    payload = {'unit': 'month', 'units': '-1'}
    auth_header = {'Authorization': f'Bearer {bitly_token}'}
    clicks_response = requests.get(
        urljoin(BITLY_API, f'bitlinks/{bitlink}/clicks/summary'),
        headers=auth_header,
        params=payload
    )
    clicks_response.raise_for_status()
    user_clicks = clicks_response.json()['total_clicks']
    return user_clicks


def is_bitlink(bitly_token, parsed_url):
    auth_header = {'Authorization': f'Bearer {bitly_token}'}
    bitlink_response = requests.get(
        urljoin(BITLY_API, f'bitlinks/{parsed_url}'),
        headers=auth_header
    )
    return bitlink_response.ok


def main():
    load_dotenv()
    bitly_token = os.environ['BITLY_TOKEN']
    user_url = input('Введите ссылку: ')
    parse_url = urlparse(user_url)
    parsed_url = f'{parse_url.netloc}{parse_url.path}'
    try:
        if not is_bitlink(bitly_token, parsed_url):
            bitlink = shorten_link(bitly_token, user_url)
            print('Битлинк:', bitlink)
        else:
            user_clicks = count_clicks(bitly_token, parsed_url)
            print('По вашей ссылке прошли:', user_clicks)
    except requests.exceptions.HTTPError:
        print('Вы ввели неправильную ссылку или указали неверный токен.')


if __name__ == "__main__":
    main()