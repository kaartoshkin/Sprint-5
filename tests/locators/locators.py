from selenium.webdriver.common.by import By

class locators():
    LOGIN_BUTTON_MAIN = By.CSS_SELECTOR, ".button_button__33qZ0" # Кнопка входа на главной
    LOGIN_BUTTON_ON_REGISTER_PAGE = By.CSS_SELECTOR, ".Auth_link__1fOlj" # Кнопка входа на странице регистрации
    LOGIN_BUTTON_ON_RESET_PASSWORD_PAGE = By.CSS_SELECTOR, ".Auth_link__1fOlj" # Кнопка входа на странице восстановления пароля
    LOGIN_BUTTON_ON_LOGIN_PAGE = By.CSS_SELECTOR, ".button_button__33qZ0" # Кнопка входа на странице входа
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//*[@id='root']/div/header/nav/a" # Кнопка личного кабинета
    REGISTER_BUTTON_ON_LOGIN_PAGE = By.CSS_SELECTOR, ".Auth_link__1fOlj" # Кнопка регистрации на странице входа
    REGISTER_BUTTON_ON_REGISTER_PAGE = By.CSS_SELECTOR, ".button_button__33qZ0" # Кнопка регистрации на странице регистрации
    NAME_INPUT = By.XPATH, "//label[text()='Имя']/following-sibling::input[1]" # Поле имени
    EMAIL_INPUT = By.XPATH, "//label[text()='Email']/following-sibling::input[1]" # Поле email
    PASSWORD_INPUT = By.XPATH, ".//input[@type='password']" # Поле пароля
    PASSWORD_ERROR = By.XPATH, ".//p[@class='input__error text_type_main-default']" # Ошибка при вводе пароля
    RESET_PASSWORD_BUTTON = By.XPATH, ".//a[text()='Восстановить пароль']" # Кнопка восстановления пароля
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2']" # Кнопка конструктора
    STELLAR_BURGERS_LOGO = By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2" # Лого
    QUIT_BUTTON = By.CSS_SELECTOR, ".Account_button__14Yp3" # Кнопка Выход
    FILLINGS_BUTTON = By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span"
    SAUCES_BUTTON = By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]/span"
    BREADROLLS_BUTTON = By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]/span"