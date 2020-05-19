from BaseTest import MainTest
from testdemo_shop.Pages.home_page import HomePage
from testdemo_shop.Pages.accesories_page import AccessoriesPage
from testdemo_shop.Pages.login_page import LoginPage
from testdemo_shop.Pages.clothes_page import ClothesPage
from testdemo_shop.Pages.art_page import ArtPage
from testdemo_shop.Locators.home_page_locs import HomePageLocators

from testdemo_shop.Helpers import operational_helpers as oh


class SmokePagesTests(MainTest):

    def test_01_title_main_page(self):
        homepage = HomePage(self.ef_driver)
        homepage.driver.get(homepage.base_url)
        home_title = homepage.driver.title
        self.assertEqual(HomePage._home_title, home_title)

    def test_02_title_art_page(self):
        art_page = ArtPage(self.ef_driver)
        art_page.driver.get(art_page.URL)
        art_title = art_page.driver.title
        self.assertEqual(ArtPage.TITLE, art_title)

    def test_03_title_clothes_page(self):
        clothes_page = ClothesPage(self.ef_driver)
        clothes_page.driver.get(clothes_page.clothes_url)
        clothes_title = clothes_page.driver.title
        self.assertEqual(ClothesPage._clothes_title, clothes_title)

    def test_04_title_accessories_page(self):
        accessories = AccessoriesPage(self.ef_driver)
        accessories.driver.get(AccessoriesPage.accessories_url)
        accessories_title = accessories.driver.title
        self.assertEqual(AccessoriesPage._accessories_title, accessories_title)

    def test_05_title_login_page(self):
        login_page = LoginPage(self.ef_driver)
        login_page.driver.get(login_page.login_url)
        login_title = login_page.driver.title
        self.assertEqual(LoginPage._login_title, login_title)

    def test_06_search_engine_return_list_of_products(self):
        search_value = 'mug'
        home_page = HomePage(self.ef_driver)
        home_page.driver.get(HomePage.main_url)
        search_field = self.ef_driver.find_element_by_css_selector(HomePageLocators.CSS_SEARCH_ENGINE)
        search_field.send_keys(search_value)
        searching_icon = self.ef_driver.find_element_by_css_selector('button i:nth-child(1)')
        searching_icon.click()
        oh.visibility_of_element_wait(self.ef_driver, 'css', 'section[id=main] h2.h2')
        list_of_elements = self.ef_driver.find_elements_by_css_selector('article.product-miniature')
        self.assertGreater(len(list_of_elements), 0, "The list of searched elements doesn't/"
                                                     "contains elements.")

    def test_07_contact_form_is_displayed(self):
        home_page = HomePage(self.ef_driver)
        home_page.driver.get(HomePage.main_url)
        contact_form_link = self.ef_driver.find_element_by_css_selector(HomePageLocators.CSS_CONTACT_FORM)
        contact_form_link.click()
        # in progress

    def test_08_modal_with_language_has_options_to_choice(self):
        raise NotImplementedError('Not implemented yet!')

    def test_09_subscribe_form_is_active(self):
        raise NotImplementedError('Not implemented yet!')

    def test_10_carousel_allows_to_swipe_elements(self):
        raise NotImplementedError('Not implemented yet!')
