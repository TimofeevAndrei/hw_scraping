import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import re

def get_headers():
    return Headers(browser="firefox", os="win").generate()


def get_text(url):
    return requests.get(url, headers=get_headers()).text


HOST = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

response = get_text(HOST)
soup = BeautifulSoup(response, features='lxml')
lenta = soup.find(id='a11y-main-content')
vacancy = lenta.findAll(class_='vacancy-serp-item__layout')
vacancy_list = []

for i in vacancy:
    # print(i)
    result = {}
    title = i.find(class_='serp-item__title')
    link_tag = title['href']
    result.update({'Url': link_tag})
    response = get_text(link_tag)
    soup = BeautifulSoup(response, features='lxml')
    name = soup.find(class_='bloko-header-section-1').text
    result.update({'title': name})
    description = soup.find(class_='vacancy-description').text
    print(description)
    if 'django' in description and 'flask' in description:
        print('match')

# print(link_list)


# template = '''
# <div class="ip" id="d_clip_button" style="cursor: pointer;">
#                                     <span>93.109.99.66</span>
#
#                                     <i class="ip-icon-shape btn-copy"></i>
#                                 </div>
# '''
#
# HOST = 'https://2ip.ru'
#
#
# response = requests.get(HOST)
# response_text = response.text
#
# soup = BeautifulSoup(response_text, features='lxml')
# d_clip_button = soup.find(id='d_clip_button')
# span = d_clip_button.find_all('span')
#
# ip_address = span.text
#
# print(f'Your IP address is {ip_address}')

