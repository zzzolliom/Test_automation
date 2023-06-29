import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_find_notebooks(driver):
    text = "Ноутбуки"
    current_url = "https://www.citilink.ru"
    driver.get(current_url)
    laptops_link = driver.find_element(By.XPATH, "//*[text()='Ноутбуки']/../..")
    laptops_link.click()
    category_title = driver.find_element(By.XPATH, "//h1")
    assert text in category_title.text

    logo = driver.find_element(By.XPATH, "(//div[@data-meta-name='Logo'])[2]")
    logo.click()

    main_page_title = driver.find_element(By.XPATH, "//div[@data-meta-name='CategoryTilesLayout__title']//h3")
    assert "Популярные категории" == main_page_title.text
def test_find_notebooks_1(driver):
    text = "Климатическая техника"
    current_url = "https://www.citilink.ru"
    driver.get(current_url)
    laptops_link = driver.find_elements(By.XPATH, "//span[contains(@class, 'app-catalog-1bu1ack')]")
    click_on_laptops_link(laptops_link, text)
    category_title = driver.find_element(By.XPATH, "//h1")
    assert text in category_title.text


def test_logo_click(driver):
    current_url = "https://www.citilink.ru/catalog/noutbuki-i-kompyutery/?ref=mainmenu"
    driver.get(current_url)
    logo_city_link = driver.find_elements(By.XPATH, "//div[@data-meta-name='Logo']")
    sleep(5)
    for element in logo_city_link:
        element.click()
    assert driver.current_url == "https://www.citilink.ru"


def click_on_laptops_link(element_list, text):
    for element in element_list:
        if element.text == text:
            element.click()


def test_product_ticket(driver):
    current_url = "https://www.citilink.ru"
    driver.get(current_url)
    click_to_get_block_specially_for_you = driver.find_element(By.XPATH,
                                                               "//div[@data-meta-name ='SnippetProductVerticalLayout']")
    click_to_get_block_specially_for_you.click()
    sleep((3))
    click_to_come_back = driver.find_element(By.XPATH, "//div[@data-meta-name='Logo']")  # не тыкает в эту кнопку
    click_to_come_back.click()
    sleep(3)
    first_in_specially_for_you_block = driver.find_element(By.XPATH,
                                                           "//div[@data-meta-name ='SnippetProductVerticalLayout']")
    element_for_find_title = first_in_specially_for_you_block.find_element('.//a')
    element_title = element_for_find_title.get_attribute('title')
    first_in_specially_for_you_block.click()
    element_title_on_page = driver.find_element(By.XPATH,
                                                "//h1[@class='e1ubbx7u0 eml1k9j0 app-catalog-tn2wxd e1gjr6xo0']").text
    assert element_title == element_title_on_page


def test_basket_btn_name(driver):
    url = "https://www.citilink.ru"
    driver.get(url)
    first_in_specially_for_you_block = driver.find_element(By.XPATH,"//div[@data-meta-name ='SnippetProductVerticalLayout']")  # провалилась в любой товар из блока "Спец для вас) Можно в любой другой блок
    first_in_specially_for_you_block.click()
    basket_button = driver.find_element(By.XPATH,
                                        "//button[@class='e11w80q30 e4uhfkv0 app-catalog-1c1fy1q e4mggex0']")  # нашла кнопку "Корзина"

    def waiter(site_connection):
        basket_button.is_displayed()

    wait = WebDriverWait(driver, 6)
    wait.untill(waiter)


def test_temp(driver):
    driver.get("https://www.python.org/")
    search_field = driver.find_element(By.CSS_SELECTOR, "#id-search-field")
    search_field.send_keys("python3")
    search_field.send_keys(Keys.ENTER)
