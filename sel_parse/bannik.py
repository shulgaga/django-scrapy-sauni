import os
import django
import sys
sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bani.settings")
django.setup()

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from parse.models import BannikUrls
from webdriver_manager.chrome import ChromeDriverManager


def get_hrefs(url):
    urls = []
    options = ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(url)
    elem = driver.find_element(By.CSS_SELECTOR, value='#column-wrapper > div.col-lg-9.col-md-12.catalog__list > div.row.get-more-container > div > button')
    sleep(1)
    try:
        while True:
            driver.execute_script("arguments[0].scrollIntoView();", elem)
            elem.click()
            sleep(1)
    except Exception:
        for url in driver.find_elements(by=By.CSS_SELECTOR, value='#column-wrapper > div.col-lg-9.col-md-12.catalog__list > div > a'):
            url = url.get_attribute('href')
            BannikUrls.objects.create(hrefs=url)
            print(url)
        driver.quit()


if __name__ == '__main__':
    get_hrefs('https://bannik.ru/msk/catalog')
    get_hrefs('https://bannik.ru/spb/catalog')
