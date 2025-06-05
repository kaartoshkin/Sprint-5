from selenium import webdriver
from locators.locators import locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome() 
driver.get("https://stellarburgers.nomoreparties.site")

button = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
button.click()

driver.quit()