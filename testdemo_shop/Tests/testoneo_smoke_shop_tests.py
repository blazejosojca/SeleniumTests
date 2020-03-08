import time

from BaseTest import MainTest
from testdemo_shop.Pages.home_page import HomePage
from testdemo_shop.Pages.accesories_page import AccessoriesPage
from testdemo_shop.Pages.login_page import LoginPage
from testdemo_shop.Pages.clothes_page import ClothesPage
from testdemo_shop.Pages.art_page import ArtPage

from testdemo_shop.Helpers import operational_helpers as oh

class SmokePagesTests(MainTest):

    def test_01_title_main_page(self):
        homepage = HomePage(self.driver)
        homepage.driver.get(homepage.base_url)
        home_title = homepage.driver.title
        self.assertEqual(HomePage._home_title, home_title)

    def test_02_title_art_page(self):
        art_page = ArtPage(self.driver)
        art_page.driver.get(art_page.URL)
        art_title = art_page.driver.title
        self.assertEqual(ArtPage.TITLE, art_title)

    def test_03_title_clothes_page(self):
        clothes_page = ClothesPage(self.driver)
        clothes_page.driver.get(clothes_page.clothes_url)
        clothes_title = clothes_page.driver.title
        self.assertEqual(ClothesPage._clothes_title, clothes_title)

    def test_04_title_accessories_page(self):
        accessories = AccessoriesPage(self.driver)
        accessories.driver.get(AccessoriesPage.accessories_url)
        accessories_title = accessories.driver.title
        self.assertEqual(AccessoriesPage._accessories_title, accessories_title)

    def test_05_title_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.driver.get(login_page.login_url)
        login_title = login_page.driver.title
        self.assertEqual(LoginPage._login_title, login_title)

    def test_06_search_engine_return_list_of_products(self):
        home_page =  HomePage(self.driver)
        home_page.driver.get(HomePage.main_url)
        search_field = self.driver.find_element_by_css_selector('input.ui-autocomplete-input')
        search_field.send_keys('mug')
        searching_icon = self.driver.find_element_by_css_selector('button i:nth-child(1)')
        searching_icon.click()
        search_results_string = oh.visibility_of_element_wait(self.driver, 'css' , 'section[id=main] h2.h2')

        print(search_results_string.text)



    def test_07_contact_form_is_displayed(self):
        # In development
        pass

    def test_08_modal_with_language_has_options_to_choice(self):
        # In development
        pass

    def test_09_subscribe_form_is_active(self):
        # In development
        pass

    def test_10_carousel_allows_to_swipe_elements(self):
        pass
