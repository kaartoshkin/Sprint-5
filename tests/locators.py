from selenium.webdriver.common.by import By

class locators():
    LOGIN_BUTTON_MAIN = By.CSS_SELECTOR, ".button_button__33qZ0" # Кнопка входа на главной
    LOGIN_BUTTON_ON_REGISTER_PAGE = By.CSS_SELECTOR, ".Auth_link__1fOlj" # Кнопка входа на странице регистрации
    LOGIN_BUTTON_ON_RESET_PASSWORD_PAGE = By.CSS_SELECTOR, ".Auth_link__1fOlj" # Кнопка входа на странице восстановления пароля
    LOGIN_BUTTON_ON_LOGIN_PAGE = By.CSS_SELECTOR, ".button_button__33qZ0" # Кнопка входа на странице входа
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']" # Кнопка личного кабинета
    REGISTER_BUTTON_ON_LOGIN_PAGE = By.CSS_SELECTOR, ".Auth_link__1fOlj" # Кнопка регистрации на странице входа
    REGISTER_BUTTON_ON_REGISTER_PAGE = By.CSS_SELECTOR, ".button_button__33qZ0" # Кнопка регистрации на странице регистрации
    NAME_INPUT = By.XPATH, "//label[text()='Имя']/following-sibling::input" # Поле имени
    EMAIL_INPUT = By.XPATH, "//label[text()='Email']/following-sibling::input" # Поле email
    PASSWORD_INPUT = By.XPATH, ".//input[@type='password']" # Поле пароля
    PASSWORD_ERROR = By.XPATH, ".//p[@class='input__error text_type_main-default']" # Ошибка при вводе пароля
    RESET_PASSWORD_BUTTON = By.XPATH, ".//a[text()='Восстановить пароль']" # Кнопка восстановления пароля
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text()='Конструктор']" # Кнопка конструктора
    STELLAR_BURGERS_LOGO = By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2" # Лого
    QUIT_BUTTON = By.CSS_SELECTOR, ".Account_button__14Yp3" # Кнопка Выход
    FILLINGS_BUTTON = By.XPATH, ".//span[text()='Начинки']" # Кнопка начинки
    FILLINGS_SECTION = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']" # Секция начинки
    SAUCES_BUTTON = By.XPATH, ".//span[text()='Соусы']" # Кнопка соусы
    SAUCES_SECTION = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']" # Секция соусы 
    BREADROLLS_BUTTON = By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']" # Кнопка булки
    BREADROLLS_SECTION = By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']" # Секция булки
    PROFILE_BUTTON_ON_PROFILE_PAGE = By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9' and text()='Профиль']" # Кнопка Профиль
    MAIN_PAGE_TEXT = By.XPATH, ".//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']"