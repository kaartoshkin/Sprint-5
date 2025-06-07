import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import locators
from generator import generate_email, generate_password

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

class TestStellarBurgers:
    def test_registraion_sucess(self, browser):

        browser.get("https://stellarburgers.nomoreparties.site")

        user_data = {
                "name": "Антон",
                "email": generate_email(),
                "password": generate_password()
            }
        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_MAIN))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_LOGIN_PAGE))
        button.click()

        name = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.NAME_INPUT))
        name.send_keys(user_data['name'])

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_REGISTER_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_ON_LOGIN_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        profile_link = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((locators.PROFILE_BUTTON_ON_PROFILE_PAGE)))
        assert profile_link.is_displayed()

        browser.quit()

    def test_registraion_error(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_LOGIN_PAGE))
        button.click()

        name = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.NAME_INPUT))
        name.send_keys('Антон')

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(generate_email())

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys('aboba')

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_REGISTER_PAGE))
        button.click()

        error_message = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.PASSWORD_ERROR))
        assert error_message.is_displayed()

        browser.quit()

    def test_quit_button(self, browser): 
        browser.get("https://stellarburgers.nomoreparties.site")

        user_data = {
                "name": "Антон",
                "email": generate_email(),
                "password": generate_password()
            }
        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_MAIN))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_LOGIN_PAGE))
        button.click()

        name = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.NAME_INPUT))
        name.send_keys(user_data['name'])

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_REGISTER_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_ON_LOGIN_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.QUIT_BUTTON))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        login_screen = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON_ON_LOGIN_PAGE))
        assert login_screen.is_displayed()

        browser.quit()

    def test_sections_navigation_fillings(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.FILLINGS_BUTTON))
        button.click()

        fillings_section = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.FILLINGS_SECTION))
        assert fillings_section.is_displayed()

        browser.quit()

    def test_sections_navigation_sauces(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.SAUCES_BUTTON))
        button.click()

        sauces_section = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.SAUCES_SECTION))
        assert sauces_section.is_displayed()

        browser.quit()

    def test_sections_navigation_breadrolls(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.SAUCES_BUTTON))
        button.click()

        WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.SAUCES_SECTION))
    
        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.BREADROLLS_BUTTON))
        button.click()

        breadrolls_section = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.BREADROLLS_SECTION))
        assert breadrolls_section.is_displayed()

        browser.quit()

    def test_constructor_button_click(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.CONSTRUCTOR_BUTTON))
        button.click()

        main_page = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_TEXT))
        assert main_page.is_displayed()

        browser.quit()

    def test_logo_click(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.STELLAR_BURGERS_LOGO))
        button.click()

        main_page = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_TEXT))
        assert main_page.is_displayed()

        browser.quit()

    def test_personal_account_button_without_registration(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        login_screen = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON_ON_LOGIN_PAGE))
        assert login_screen.is_displayed()

        browser.quit()

    def test_personal_account_button_with_registration(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site")

        user_data = {
                "name": "Антон",
                "email": generate_email(),
                "password": generate_password()
            }
        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_MAIN))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_LOGIN_PAGE))
        button.click()

        name = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.NAME_INPUT))
        name.send_keys(user_data['name'])

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_REGISTER_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_ON_LOGIN_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        profile_link = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((locators.PROFILE_BUTTON_ON_PROFILE_PAGE)))
        assert profile_link.is_displayed()

        browser.quit()

    def test_login_by_personal_account_button(self, browser): 
        browser.get("https://stellarburgers.nomoreparties.site")

        user_data = {
                "name": "Антон",
                "email": generate_email(),
                "password": generate_password()
            }
        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_LOGIN_PAGE))
        button.click()

        name = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.NAME_INPUT))
        name.send_keys(user_data['name'])

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_REGISTER_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_ON_LOGIN_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        profile_link = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((locators.PROFILE_BUTTON_ON_PROFILE_PAGE)))
        assert profile_link.is_displayed()

        browser.quit()

    def test_login_by_button_on_registration_page(self, browser): 
        browser.get("https://stellarburgers.nomoreparties.site")

        user_data = {
                "name": "Антон",
                "email": generate_email(),
                "password": generate_password()
            }
        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_MAIN))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_LOGIN_PAGE))
        button.click()

        name = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.NAME_INPUT))
        name.send_keys(user_data['name'])

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_REGISTER_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_LOGIN_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_ON_REGISTER_PAGE))
        button.click()
        
        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_ON_LOGIN_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        profile_link = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((locators.PROFILE_BUTTON_ON_PROFILE_PAGE)))
        assert profile_link.is_displayed()

        browser.quit()

    def test_login_by_button_on_password_reset_page(self, browser): 
        browser.get("https://stellarburgers.nomoreparties.site")

        user_data = {
                "name": "Антон",
                "email": generate_email(),
                "password": generate_password()
            }
        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_LOGIN_PAGE))
        button.click()

        name = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.NAME_INPUT))
        name.send_keys(user_data['name'])

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_REGISTER_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.RESET_PASSWORD_BUTTON))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_ON_RESET_PASSWORD_PAGE))
        button.click()

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_ON_LOGIN_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        profile_link = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((locators.PROFILE_BUTTON_ON_PROFILE_PAGE)))
        assert profile_link.is_displayed()

        browser.quit()

    def test_login_by_button_on_main_page(self, browser): 
        browser.get("https://stellarburgers.nomoreparties.site")

        user_data = {
                "name": "Антон",
                "email": generate_email(),
                "password": generate_password()
            }
        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_MAIN))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_LOGIN_PAGE))
        button.click()

        name = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.NAME_INPUT))
        name.send_keys(user_data['name'])

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.REGISTER_BUTTON_ON_REGISTER_PAGE))
        button.click()

        browser.get("https://stellarburgers.nomoreparties.site")

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_MAIN))
        button.click()

        email = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.EMAIL_INPUT))
        email.send_keys(user_data["email"])

        password = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PASSWORD_INPUT))
        password.send_keys(user_data["password"])

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON_ON_LOGIN_PAGE))
        button.click()

        button = WebDriverWait(browser, 3).until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
        button.click()

        profile_link = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located((locators.PROFILE_BUTTON_ON_PROFILE_PAGE)))
        assert profile_link.is_displayed()

        browser.quit()