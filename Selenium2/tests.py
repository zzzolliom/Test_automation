import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def test_sign_up(driver, generate_random_name):
    register_header_text = 'Регистрация'
    enter_header_text = 'Вход'
    url = 'https://stellarburgers.nomoreparties.site/'
    driver.get(url)
    sign_in_button = driver.find_element(By.XPATH,"//button[contains(text(), 'Войти в аккаунт')]")
    # sign_in_button = driver.find_element("//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    sign_in_button.click()
    link_to_register = driver.find_element(By.XPATH, "//a[@href = '/register']")
    link_to_register.click()
    register_header = driver.find_element(By.XPATH, "//h2[text()='Регистрация']")
    assert register_header_text in register_header.text

    name_input = driver.find_element(By.XPATH, "(//input)[1]" )      #"//label[text() ='Имя']" не тыкает
    name = generate_random_name
    name_input.send_keys(name)
    email_input = driver.find_element(By.XPATH, "(//input)[2]")
    email_input.send_keys(f"{name}@gmail.com")

    password_input = driver.find_element(By.XPATH, "(//input)[3]")
    password_input.send_keys(f"{name}+%#$!123")

    registration_confirm = driver.find_element(By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    registration_confirm.click()
    wait = WebDriverWait(driver, 10)  # Максимальное время ожидания - 10 секунд (можно изменить)
    locator = (By.XPATH, "//h2[text()='Вход']")
    enter_header = wait.until(EC.presence_of_element_located(locator))
    assert enter_header.is_displayed()
     # assert enter_header_text in enter_header.text # тут лучше проверить код ответа апи, потому что не понятно произошла ли регистрация в интерфейсе, но я пока не умею))))

def test_sign_in(driver, email,password): #куда лчше складывать тестовые данные?
    url = 'https://stellarburgers.nomoreparties.site/'
    driver.get(url)
    sign_in_button = driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']")
    sign_in_button.click()
    email_input = driver.find_element(By.XPATH, "(//input)[1]")
    password_input = driver.find_element(By.XPATH, "(//input)[2]")
    enter_button = driver.find_element(By.XPATH, "//button[text()='Войти']" )
    email_input.send_keys(email)
    password_input.send_keys(password)
    enter_button.click()
    wait = WebDriverWait(driver, 10)
    write_up_order_element = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))
    assert write_up_order_element.is_displayed()


def test_logout(driver,api_authorization_token):
    token = api_authorization_token
    url = 'https://stellarburgers.nomoreparties.site/'
    cookie = {
        "name": "Authorization",
        "value": token,
        "domain": "stellarburgers.nomoreparties.site",
        "path": "/"
    }
    driver.add_cookie(cookie)
    driver.get(url)
    driver.refresh() # до этого места похоже, что надо вынести это в фикстуру (Только url на главную старницу наслать) , но я не поняла, что и как из этой фикстуры получать
    personal_account = driver.find_element(By.XPATH, "//p[text() ='Личный Кабинет']")
    personal_account.click()
    sign_out_button = driver.find_element(By.XPATH, "//button[text() = 'Выход']")
    sign_out_button.click()
    wait = WebDriverWait(driver, 10)
    enter_header = wait.until(EC.presence_of_element_located(("//h2[text()='Вход']")))
    assert enter_header.is_displayed()
