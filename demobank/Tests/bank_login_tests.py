import time

from BaseTest import MainTest

from demobank.Pages.login_page import LoginPage
from demobank.Locators.login_page_locs import LoginPageLocators
from demobank.Helpers import operational_helpers as oh

class LoginPageTests(MainTest):

    def test_exact_text_for_login_form_header(self):
        self.driver.get(LoginPage._url)
        login_form_header_element = self.driver.find_element_by_xpath(LoginPageLocators.XPATH_HEADER)
        login_form_header_text = login_form_header_element.text
        expected_text = 'Wersja demonstracyjna serwisu demobank'

        self.assertEqual(expected_text, login_form_header_text,
                         f'Expected title differ from actual title for page url: {LoginPage._url}')

    def test_button_dalej_is_disabled_when_login_input_is_empty(self):

        self.driver.get(LoginPage._url)
        login_form_input_element = self.driver.find_element_by_xpath(LoginPageLocators.XPATH_LOGIN_INPUT_FIELD)
        login_form_input_element.clear()
        login_next_button_element = self.driver.find_element_by_xpath(LoginPageLocators.XPATH_NEXT_BUTTON)
        login_next_button_disabled = login_next_button_element.get_property('disabled')
        self.assertEqual(True, login_next_button_disabled,
                         f'Expected state of "dalej" button: True , differ from actual: {login_next_button_disabled} , for page url: {LoginPage._url}')

    def test_display_error_message_when_user_submit_less_than_8_signs(self):
        self.driver.get(LoginPage._url)
        login_form_input_element = self.driver.find_element_by_xpath(LoginPageLocators.XPATH_LOGIN_INPUT_FIELD)
        login_text = '1234567'
        login_form_input_element.send_keys(login_text)
        hint_button_element = self.driver.find_element_by_xpath(
            '//*[@id="login_id_container"]//*[@class="i-hint-white tooltip widget-info"]')
        hint_button_element.click()
        warning_message_element = self.driver.find_element_by_xpath('//*[@class="error"]')
        warning_message_text = warning_message_element.text
        self.assertEqual('identyfikator ma min. 8 znaków', warning_message_text,
                         f'Expected warning message differ from actual one for url: {LoginPage._url}')

    def test_button_dalej_respond_when_enters_8_signs_id(self):
        # self.driver.get(LoginPage._url)
        page = LoginPage(self.driver)
        self.driver.get(page._url)
        page.find_and_fill_by_xpath('//*[@id="login_id"]', '12345678')
        page.find_and_click_by_xpath('//*[@id="login_next"]')
        login_next_button_element = oh.visibility_of_element_wait(self.driver, LoginPageLocators.XPATH_NEXT_BUTTON)

        new_login_button_text = login_next_button_element.text
        self.assertEqual('zaloguj się', new_login_button_text,
                         f'Expected login button text: zaloguj się , differ from actual {new_login_button_text}')

    def test_correct_popup_text(self):
        page = LoginPage(self.driver)
        self.driver.get(page._url)
        page.find_and_click_by_xpath('//*[@id="ident_rem"]')

        popup_text_element = oh.visibility_of_element_wait(self.driver, LoginPageLocators.XPATH_POPUP)
        popup_text_element_text = popup_text_element.text
        self.assertEqual('ta funkcja jest niedostępna', popup_text_element_text,
                         f'Expected login button text differ from actual: {popup_text_element_text}')

    def test_correct_login_from_login_etap2(self):
        self.driver.get(LoginPage._url)
        # finding login input box and sending value
        login_input_element = self.driver.find_element_by_xpath(LoginPageLocators.XPATH_LOGIN_INPUT_FIELD)
        login_input_element.clear()
        login_input_element.send_keys('kocur131')
        # finding login password box and sending value
        password_input_element = self.driver.find_element_by_xpath(LoginPageLocators.XPATH_LOGIN_PASSWORD_FIELD)
        password_input_element.click()

        password_input_element.send_keys('123456789')
        # finding button 'zaloguj'
        button_next_element = self.driver.find_element_by_xpath('//*[@id="login_next"]')
        button_next_element.click()
        messages_element = oh.visibility_of_element_wait(self.driver, LoginPageLocators.XPATH_MESSAGE)
        messages_element_text = messages_element.text
        self.assertEqual('Brak wiadomości', messages_element_text,
                         f'Expected login button text differ from actual: {messages_element_text}')