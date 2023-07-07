from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=312322e5-94fa-41eb-880e-6e97327a1605&theme&auth_type'
        super().__init__(web_driver, url)

    phone = WebElement(id='username')
    email = WebElement(id='username')
    login = WebElement(id='username')
    ls = WebElement(id='username')
    password = WebElement(id='password')
    btn = WebElement(id='kc-login')
    recovery = WebElement(id='forgot_password')
    registration = WebElement(id='kc-register')
    code = WebElement(id='back_to_otp_btn')
    auth_code = WebElement(id='address')
    get_code = WebElement(id='otp_get_code')
    rt_code = WebElement(id='rt-code-0')
    captcha = WebElement(class_name='rt-captcha__image')
    symbol = WebElement(id='captcha')
    contin = WebElement(id='reset')
    new_pass = WebElement(id='password-new')
    confirm = WebElement(id='confirmation')
    save = WebElement(id='t-btn-reset-pass')
    name = WebElement(name='firstName')
    lastname = WebElement(name='lastName')
    region = WebElement(autocomplete='new-password')
    email_or_phone = WebElement(id='address')
    pass_conf = WebElement(id='password-confirm')
    register = WebElement(name='register')
    conf_reg_text = WebElement(h1='Подтверждение email')
    tab_phone = WebElement(id='t-btn-tab-phone')
    tab_email = WebElement(id='t-btn-tab-mail')
    tab_login = WebElement(id='t-btn-tab-login')
    tab_ls = WebElement(id='t-btn-tab-ls')
    main_tab = WebElement(class_name='rt-tab rt-tab--small rt-tab--active')
    err_message = WebElement(id='form-error-message')
    left= WebElement(id='page-left')
    err_text = WebElement(class_name='name-container')
    err_text_ph = WebElement(class_name='register-form__address')
    err_text_ps = WebElement(class_name='new-password-container')
    code_send = WebElement(class_name='register-confirm-form-container__desc')
    log_out = WebElement(id='logout-btn')

class AuthPage_2(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?response_type=code&scope=openid&client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Flk.rt.ru%252F&state=%7B%22uuid%22%3A%222B1214F2-EB0D-4BEE-BF30-2BE97D3C2BBF%22%7D'
        super().__init__(web_driver, url)

    email_or_phone = WebElement(id='address')
    get_code = WebElement(name='otp_get_code')
    confirm = WebElement(class_name='card-container__title')
