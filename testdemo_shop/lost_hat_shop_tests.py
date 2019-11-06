import unittest
from BaseTest import MainTest
from testdemo_shop.locators import (LoginPageLocators,
                                    AccountPageLocators,
                                    ArticlesPageLocators,
                                    HomePageLocators)
from testdemo_shop.pages import (LoginPage,
                                 AccountPage,
                                 ArticlePage,
                                 HomePage)
from testdemo_shop.helpers.functional_helper import user_login


class SimpleTests(MainTest):

    def test_01_check_defined_header_is_on_login_site(self):
        expected_text = LoginPage.HEADER_TEXT
        self.driver.get(LoginPage.login_url)
        self.assert_element_text(LoginPageLocators.XPATH_HEADER_MESSAGE, expected_text)

    def test_02_check_login_to_registered_account_wrong_both_credentials(self):
        print(self.driver.current_url)
        login_page = LoginPage(self.driver)
        self.driver.get(login_page.login_url)
        login_page.login_with_invalid_credentials()
        print(self.driver.current_url)
        self.assert_element_text(LoginPageLocators.XPATH_AUTH_FAILED, LoginPage.FAILED_MESSAGE)

    def test_03_check_article_name(self):
        article_page = ArticlePage(self.driver)
        self.driver.get(article_page.URL)
        expected_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        self.assert_element_text(ArticlesPageLocators.XPATH_ARTICLE_NAME, expected_name)

    def test_04_check_article_price(self):
        article_page = ArticlePage(self.driver)
        self.driver.get(article_page.URL)
        expected_price = 'PLN23.52'
        self.assert_element_text(ArticlesPageLocators.XPATH_ARTICLE_PRICE, expected_price)

    def test_05_check_login_to_registered_account(self):
        expected_header = AccountPage.ACCOUNT_TITLE
        user_login(self.driver)
        self.assert_element_text(AccountPageLocators.XPATH_ACCOUNT_HEADER, expected_header)

class LostHatFrontPageTests(MainTest):

    def test_01_check_displaying_slider(self):
        homepage = HomePage(self.driver)
        homepage.driver.get(homepage.base_url)
        homepage_slider = homepage.driver.find_element_by_css_selector(HomePageLocators.CSS_SLIDER)

        self.assertTrue(homepage_slider)

    def test_02_slider_minimum_size(self):
        expected_size = {
            "height": "",
            "width": ""
        }
        homepage = HomePage(self.driver)
        homepage.driver.get(homepage.base_url)
        homepage_slider = homepage.driver.find_element_by_css_selector(HomePageLocators.CSS_SLIDER)
        if self.driver.name == 'firefox':
            expected_size["height"] = 340.0
            expected_size["width"] = 1110.0
        elif self.driver.name == 'chrome':
            expected_size["height"] = 340
            expected_size["width"] = 690

        with self.subTest('Element height'):
            self.assertLessEqual(expected_size["height"], homepage_slider.size["height"])

        with self.subTest('Element width'):
            self.assertLessEqual(expected_size["width"], homepage_slider.size["width"])




        self.assertLessEqual(expected_size["height"], homepage_slider.size["height"])
        self.assertLessEqual(expected_size["width"], homepage_slider.size["width"])

    def test_03_check_slider_contains_number_of_slides(self):
        number_of_slides = 3
        homepage = HomePage(self.driver)
        homepage.driver.get(homepage.base_url)
        slider_elements = homepage.driver.find_elements_by_css_selector(HomePageLocators.CSS_SLIDER_ELEMENTS)
        number_of_slider_elements = (len(slider_elements))
        #
        self.assertEqual(number_of_slides, number_of_slider_elements)

    def test_04_slides_have_required_title_text(self):
        homepage = HomePage(self.driver)
        homepage.driver.get(homepage.base_url)
        slides_titles = homepage.driver.find_elements_by_css_selector(HomePageLocators.CSS_SLIDES_TITLES)
        expected_text = "sample"

        for slide in slides_titles:
            slide_text_lower = slide.get_attribute("textContent").lower()
            with self.subTest(slide_text_lower):
                self.assertIn(expected_text,slide_text_lower,
                              f"Slides doesn't have expected text")


        # self.assertListEqual(required_list, slides_titles_list)

    def test_05_articles_required_number_on_page(self):
        homepage = HomePage(self.driver)
        homepage.driver.get(homepage.base_url)
        articles_miniatures = homepage.driver.find_elements_by_css_selector(HomePageLocators.CSS_ARTICLE_MINIATURE)
        number_of_articles_on_homepage = len(articles_miniatures)
        self.assertEqual(number_of_articles_on_homepage, 8 )

    def test_06_expected_test_included_in_string(self):
        expected_text = 'star'
        list_of_items = ['stargate', 'starship', 'cat', 'stardust', 'startreck', 'dog']

        for title_element in list_of_items:
            print(f'Text: {title_element}')

        for item in list_of_items:
            with self.subTest(item):
                self.assertIn(expected_text, item,
                          f'Slides does not contain expected text for page')


if __name__ == '__main__':
    unittest.main()
