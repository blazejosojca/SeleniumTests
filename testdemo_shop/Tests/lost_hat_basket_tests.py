import unittest

from BaseTest import MainTest
from testdemo_shop.Locators.art_page_locs import ArtPageLocators
from testdemo_shop.Locators.art_sub_page_locs import ArtSubPageLocators
from testdemo_shop.Pages.art_page import ArtPage
from testdemo_shop.Pages.article_sub_page import ArticleSubPage
from testdemo_shop.Helpers import operational_helpers as oh


class BasketTests(MainTest):

    def test_01_check_article_name(self):
        article_page = ArticleSubPage(self.driver)
        self.driver.get(article_page.URL)

        expected_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        article_name = ArtSubPageLocators.XPATH_ARTICLE_NAME

        self.assert_element_text(article_name, expected_name)

    def test_02_check_article_price(self):
        article_page = ArticleSubPage(self.driver)
        self.driver.get(article_page.URL)

        expected_price = 'PLN23.52'
        article_price = ArtSubPageLocators.XPATH_ARTICLE_PRICE

        self.assert_element_text(article_price, expected_price)

    def test_03_product_added_to_basket(self):
        articles_page = ArtPage(self.driver)
        self.driver.get(articles_page.URL)

        expected_modal_text = '\ue876Product successfully added to your shopping cart'
        item_xpath = ArtPageLocators.XPATH_MOUNTAIN_FOX
        shopping_cart_btn_xpath = ArtPageLocators.XPATH_BTN_ADD_TO_CHART
        confirmation_modal_title_xpath = ArtPageLocators.XPATH_MODAL_TITLE

        articles_page.find_and_click_by_xpath(item_xpath)
        button = self.driver.find_element_by_xpath(shopping_cart_btn_xpath)
        button.click()

        confirmation_modal_element = oh.visibility_of_element_wait(self.driver, 'xpath', confirmation_modal_title_xpath, 5)

        self.assertEqual(expected_modal_text, confirmation_modal_element.text)
        self.assertIn(expected_modal_text, confirmation_modal_element.text)


if __name__ == '__main__':
    unittest.main()
