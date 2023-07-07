import time
import pytest
import random
import selenium
from pages.auth_page import AuthPage, AuthPage_2
from settings import *
from selenium import webdriver
from pages.base import WebPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

#1 авторизация по email
def test_authorisation_email(web_browser):

    page = AuthPage(web_browser)
    if page.captcha.find():
        pytest.skip("captcha")
    else:
        page.email.send_keys(valid_email)
        page.password.send_keys(valid_password)
        page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() and page.log_out.find()


#2 авторизация по телефону
def test_authorisation_phone(web_browser):

    page = AuthPage(web_browser)
    if page.captcha.find():
        pytest.skip("captcha")
    else:
        page.phone.send_keys(valid_phone)
        page.password.send_keys(valid_password)
        page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() and page.log_out.find()


#3 авторизация по ЛС
def test_authorisation_check(web_browser):

    page = AuthPage(web_browser)
    if page.captcha.find():
        pytest.skip("captcha")
    else:
        page.ls.send_keys(valid_ls)
        page.password.send_keys(valid_password)
        page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() and page.log_out.find()

#4 авторизация по логину
def test_authorisation_login(web_browser):

    page = AuthPage(web_browser)
    if page.captcha.find():
        pytest.skip("captcha")
    else:
        page.login.send_keys(valid_login)
        page.password.send_keys(valid_password)
        page.btn.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() and page.log_out.find()


#5 переключение табов при авторизации ЛС
@pytest.mark.parametrize('ls',[valid_email,valid_phone, valid_login],
                         ids=['email','phone','login'])
def test_tab_ls(web_browser,ls):
    page=AuthPage(web_browser)
    page.tab_ls.click()
    page.ls.send_keys(ls)
    page.password.send_keys(valid_password)

    assert page.tab_email.get_attribute('ID') =='t-btn-tab-mail' or\
           page.tab_phone.get_attribute('ID') =='t-btn-tab-phone' or\
           page.tab_login.get_attribute('ID') =='t-btn-tab-login'

#6 переключение табов при авторизации телефону
@pytest.mark.parametrize('phone',[valid_email, valid_login,valid_ls],
                         ids=['email','phone','login'])
def test_tab_phone(web_browser,phone):
    page=AuthPage(web_browser)
    page.tab_phone.click()
    page.phone.send_keys(phone)
    page.password.send_keys(valid_password)

    assert page.tab_email.get_attribute('ID') =='t-btn-tab-mail' or\
           page.tab_phone.get_attribute('ID') =='t-btn-tab-ls' or\
           page.tab_login.get_attribute('ID') =='t-btn-tab-login'


#7 переключение табов при авторизации email
@pytest.mark.parametrize('email',[valid_phone, valid_login,valid_ls],
                         ids=['email','phone','login'])
def test_tab_email(web_browser,email):
    page=AuthPage(web_browser)
    page.tab_email.click()
    page.email.send_keys(email)
    page.password.send_keys(valid_password)

    assert page.tab_email.get_attribute('ID') =='t-btn-tab-ls' or\
           page.tab_phone.get_attribute('ID') =='t-btn-tab-phone' or\
           page.tab_login.get_attribute('ID') =='t-btn-tab-login'


#8 переключение табов при авторизации login
@pytest.mark.parametrize('login',[valid_phone, valid_email,valid_ls],
                         ids=['email','phone','login'])
def test_tab_login(web_browser,login):
    page=AuthPage(web_browser)
    page.tab_login.click()
    page.login.send_keys(login)
    page.password.send_keys(valid_password)

    assert page.tab_email.get_attribute('ID') =='t-btn-tab-ls' or\
           page.tab_phone.get_attribute('ID') =='t-btn-tab-phone' or\
           page.tab_login.get_attribute('ID') =='t-btn-tab-login'


#9 Авторизация по почте негативный
@pytest.mark.parametrize('email',[not_valid_email,valid_email,special,russian_chars(),' '],
                         ids=['invalid_mail','valid_mail','special','cyrillic','empty'])
@pytest.mark.parametrize('password',[valid_password, not_valid_password,' '],
                         ids=['valid_pass','invalid_pass','empty'])
def test_authorisation_email_negative(web_browser,email,password):

    page = AuthPage(web_browser)
    if page.captcha.find():
        pytest.skip("captcha")
    else:
        page.tab_email.click()
        page.email.send_keys(email)
        page.password.send_keys(password)
        page.btn.click()
    assert page.err_message.get_attribute('ID')=='form-error-message' and page.err_message.get_text() == 'Неверный логин или пароль'

#10 негативный по телефону
@pytest.mark.parametrize('phone',[not_valid_phone,valid_phone,special,russian_chars(),' '],
                         ids=['invalid_phone','valid_phone','special','cyrillic','empty'])
@pytest.mark.parametrize('password',[valid_password, not_valid_password,' '],
                         ids=['valid_pass','invalid_pass','empty'])
def test_authorisation_phone_negative(web_browser,phone,password):

    page = AuthPage(web_browser)
    if page.captcha.find():
        pytest.skip("captcha")
    else:
        page.phone.send_keys(phone)
        page.password.send_keys(password)
        page.btn.click()
    assert page.err_message.get_attribute('ID')=='form-error-message' and page.err_message.get_text() == 'Неверный логин или пароль'

# 11 негативный по логину
@pytest.mark.parametrize('login',[not_valid_login,valid_login,special,russian_chars(),' '],
                         ids=['invalid_login','valid_login','special','cyrillic','empty'])
@pytest.mark.parametrize('password',[valid_password, not_valid_password,' '],
                         ids=['valid_pass','invalid_pass','empty'])
def test_authorisation_login_negative(web_browser,login,password):

    page = AuthPage(web_browser)
    if page.captcha.find():
        pytest.skip("captcha")
    else:
        page.login.send_keys(login)
        page.password.send_keys(password)
        page.btn.click()
    assert page.err_message.get_attribute('ID')=='form-error-message' and page.err_message.get_text() == 'Неверный логин или пароль'


# 12 негативный по ЛС
@pytest.mark.parametrize('ls',[not_valid_ls,valid_ls,special,russian_chars(),' '],
                         ids=['invalid_ls','valid_ls','special','cyrillic','empty'])
@pytest.mark.parametrize('password',[valid_password, not_valid_password,' '],
                         ids=['valid_pass','invalid_pass','empty'])
def test_authorisation_ls_negative(web_browser,ls,password):

    page = AuthPage(web_browser)
    if page.captcha.find():
        pytest.skip("captcha")
    else:
        page.ls.send_keys(ls)
        page.password.send_keys(password)
        page.btn.click()
    assert page.err_message.get_attribute('ID')=='form-error-message' and page.err_message.get_text() == 'Неверный логин или пароль'

#13 проверка текста в левой части страницы авторизации
def test_authorisation_page_check(web_browser):

    page = AuthPage(web_browser)

    assert 'Личный кабинет' in page.left.get_text()


#14 провекра текста в левой части страницы регистрации
@pytest.mark.negativ
def test_registrstion_page_check(web_browser):

    page = AuthPage(web_browser)
    page.registration.click()

    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration?client_id=account_b2c&tab_id=' in page.get_current_url()
    assert 'Личный кабинет' in page.left.get_text()

#15 негативные проверки поля "Имя" на странице регистрации
@pytest.mark.parametrize('name',['',cyrillic2,eng,russian_chars(),special,number,numb_abc ],
                         ids=['empty','less than 2','english','more than 30','special','number','numbers_letters'])
def test_reg_field_name(web_browser,name):
    page = AuthPage(web_browser)
    page.registration.click()
    page.name.send_keys(name)
    page.name.send_keys(Keys.ENTER)

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов' in page.err_text.get_text()


#16 негативные проверки поля "Фамилия" на странице регистрации
@pytest.mark.negativ
@pytest.mark.parametrize('lastname',['',cyrillic2,eng,russian_chars(),special,number,numb_abc ],
                         ids=['empty','less than 2','english','more than 30','special','number','numbers_letters'])
def test_reg_field_lastname(web_browser,lastname):
    page = AuthPage(web_browser)
    page.registration.click()
    page.lastname.send_keys(lastname)
    page.lastname.send_keys(Keys.ENTER)

    assert 'Необходимо заполнить поле кириллицей. От 2 до 30 символов' in page.err_text.get_text()


#17 Негативные проверки поля "телефон или email"
@pytest.mark.negativ
@pytest.mark.parametrize('email_or_phone',['',eng,russian_chars(),special,number,numb_abc,sym255,sym1001],
                         ids=['empty','english','cyrillic','special','number','numbers_letters','symbols255','symbols1001'])
def test_reg_field_email_or_phone(web_browser,email_or_phone):
    page = AuthPage(web_browser)
    page.registration.click()
    page.email_or_phone.send_keys(email_or_phone)
    page.email_or_phone.send_keys(Keys.ENTER)

    assert 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru' in page.err_text_ph.get_text()


#18 негативные проверки поля "Пароль"
@pytest.mark.parametrize('password',['',eng,russian_chars(),special,number,numb_abc,sym255,sym1001],
                         ids=['empty','english','cyrillic','special','number','numbers_letters','symbols255','symbols1001'])
def test_reg_field_password(web_browser,password):
    page = AuthPage(web_browser)
    page.registration.click()
    page.password.send_keys(password)
    page.password.send_keys(Keys.ENTER)

    assert 'Длина пароля должна быть не менее 8 символов' in page.err_text_ps.get_text() or \
           'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру' in page.err_text_ps.get_text() or \
           'Пароль должен содержать хотя бы одну заглавную букву' in page.err_text_ps.get_text()


#19 авторизация по коду
def test_authorisation_code_phone(web_browser):

    page = AuthPage_2(web_browser)
    if page.captcha.find():
        pytest.skip("captcha")
    else:
        page.email_or_phone.send_keys(valid_phone)
        page.get_code.click()

    assert page.confirm.get_text()=='Код подтверждения отправлен'
    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate?execution=' in page.get_current_url()

#20 регистрация пользователя по email
def test_registration_email(web_browser):
    page = AuthPage(web_browser)
    page.registration.click()
    page.name.send_keys(name)
    page.lastname.send_keys(lastname)
    page.email_or_phone.send_keys(new_email)
    page.password.send_keys(valid_password)
    page.pass_conf.send_keys(valid_password)
    page.register.click()

    assert 'Kод подтверждения отправлен на адрес' in page.code_send.get_text()


#21 регистрация пользователя по телефону
def test_registration_phone(web_browser):
    page = AuthPage(web_browser)
    page.registration.click()
    page.name.send_keys(name)
    page.lastname.send_keys(lastname)
    page.email_or_phone.send_keys(not_valid_phone)
    page.password.send_keys(valid_password)
    page.pass_conf.send_keys(valid_password)
    page.register.click()

    assert 'Kод подтверждения отправлен на номер' in page.code_send.get_text()



