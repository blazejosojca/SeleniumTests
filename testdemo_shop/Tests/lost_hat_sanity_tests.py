from BaseTest import MainTest
from testdemo_shop.Locators.account_page_locs import AccountPageLocators
from testdemo_shop.Locators.home_page_locs import HomePageLocators
from testdemo_shop.Pages.home_page import HomePage
from testdemo_shop.Pages.register_page import RegisterPage

from testdemo_shop.Helpers.functional_helper import user_login

from testdemo_shop.Helpers import operational_helpers as oh


class SanityPageTests(MainTest):

    def test_01_check_login_to_registered_account(self):
        user_login(self.ef_driver)
        self.assert_element_text(AccountPageLocators.XPATH_USER_NAME, RegisterPage.TEST_USER_NAME)

    def test_02_check_search_engine(self):
        search_value = 'hummingbird'
        home_page = HomePage(self.ef_driver)
        home_page.driver.get(HomePage.main_url)
        search_field = self.ef_driver.find_element_by_css_selector(HomePageLocators.CSS_SEARCH_ENGINE)
        search_field.send_keys(search_value)
        searching_icon = self.ef_driver.find_element_by_css_selector(HomePageLocators.CSS_SEARCH_ICON)
        searching_icon.click()
        oh.visibility_of_element_wait(self.ef_driver, 'css', 'section[id=main] h2.h2')
        list_of_elements = self.ef_driver.find_elements_by_css_selector('h1[itemprop="name"]')
        found_elements = 0
        for element in list_of_elements:
            if search_value in element.get_attribute('innerText').lower():
                found_elements += 1
            return found_elements
        self.assertEqual(found_elements, len(list_of_elements))

    def test_03_check_currency_of_products(self):
        polish_currency = 'PLN'
        home_page = HomePage(self.ef_driver)
        home_page.driver.get(HomePage.main_url)
        prices_elements = self.ef_driver.find_elements_by_css_selector(HomePageLocators.CSS_PRICE_ELEMENTS)
        for element in prices_elements:
            self.assertIn(polish_currency, element.get_attribute('textContent'),
                          f"Expected text not found in product description for page")
