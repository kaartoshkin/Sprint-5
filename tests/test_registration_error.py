from selenium import webdriver
from locators.locators import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tools.generator import generate_email

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site")

button = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
button.click()

button = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_LOGIN_PAGE))
button.click()

name = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.NAME_INPUT))
name.send_keys('Антон')

email = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
email.send_keys(generate_email())

password = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
password.send_keys('aboba')

button = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_REGISTER_PAGE))
button.click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locators.PASSWORD_ERROR))

driver.quit()