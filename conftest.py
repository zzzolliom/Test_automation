import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import random
import requests



@pytest.fixture()
def driver():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture()
def generate_random_name():
    vowels = 'aeiou'
    consonants = 'dcdfghjklmnopqrstvwxz'
    name = random.choice(consonants).upper()
    name += random.choice(vowels)
    name += random.choice(consonants)
    name += random.choice(vowels)
    name += random.choice(consonants)
    name += random.choice(vowels)
    yield name

@pytest.fixture()
def email():
    email = 'Jlga@gmail.com'
    yield email


@pytest.fixture()
def password():
    password = 'Jlga%#$!123'
    yield password

@pytest.fixture()
def api_authorization_token():
    url = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    auth_data = {
    "email": "Jlga@gmail.com",
    "password": "Jlga%#$!123"
}
    response = requests.post(url, auth_data)
    token = response.json().get("accessToken")
    yield token

