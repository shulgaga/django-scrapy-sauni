import os
import django
import sys
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bani.settings")
django.setup()

from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from parse.models import ZoonUrls
from webdriver_manager.chrome import ChromeDriverManager



urls = [
        'https://spb.zoon.ru/sauna/',
        'https://ekb.zoon.ru/sauna/',
        'https://nsk.zoon.ru/sauna/',
        'https://kazan.zoon.ru/sauna/',
        'https://nn.zoon.ru/sauna/',
        'https://chelyabinsk.zoon.ru/sauna/',
        'https://samara.zoon.ru/sauna/',
        'https://omsk.zoon.ru/sauna/',
        'https://ufa.zoon.ru/sauna/',
        'https://rostov.zoon.ru/sauna/',
        'https://krasnoyarsk.zoon.ru/sauna/'
]


def get_zoon_html(url):
    options = ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')

    info = []

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    try:
        driver.get(url=url)
        sleep(3)
        while True:
                find_more_element = driver.find_element(by=By.CLASS_NAME, value='catalog-button-showMore')
                actions = ActionChains(driver)
                actions.move_to_element(find_more_element).perform()
                sleep(3)
    except Exception:
        html = driver.page_source
    finally:
        driver.close()
        driver.quit()

    soup = BeautifulSoup(html, 'lxml').find_all(class_='minicard-item__title')
    for href in soup:
        href = href.find('a').get('href')
        ZoonUrls.objects.create(hrefs=href)
        print(href)


if __name__ == '__main__':
    urls = [
        'https://spb.zoon.ru/sauna/',
        'https://ekb.zoon.ru/sauna/',
        'https://nsk.zoon.ru/sauna/',
        'https://kazan.zoon.ru/sauna/',
        'https://nn.zoon.ru/sauna/',
        'https://chelyabinsk.zoon.ru/sauna/',
        'https://samara.zoon.ru/sauna/',
        'https://omsk.zoon.ru/sauna/',
        'https://ufa.zoon.ru/sauna/',
        'https://rostov.zoon.ru/sauna/',
        'https://krasnoyarsk.zoon.ru/sauna/'
    ]
    for one in urls:
        get_zoon_html(one)
