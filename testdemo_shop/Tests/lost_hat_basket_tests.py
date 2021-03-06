import unittest

from testdemo_shop.BaseTest import BaseTestClass
from testdemo_shop.Locators.art_page_locs import ArtPageLocators
from testdemo_shop.Locators.art_sub_page_locs import ArtSubPageLocators
from testdemo_shop.Pages.art_page import ArtPage
from testdemo_shop.Pages.article_sub_page import ArticleSubPage
from testdemo_shop.Helpers import operational_helpers as oh
from testdemo_shop.Helpers.wrappers import screenshot_decorator


class BasketTests(BaseTestClass):

    @screenshot_decorator
    def test_01_check_article_name(self):
        article_page = ArticleSubPage(self.ef_driver)
        self.ef_driver.get(article_page.URL)

        expected_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        article_name = ArtSubPageLocators.XPATH_ARTICLE_NAME

        self.assert_element_text(article_name, expected_name)

    @screenshot_decorator
    def test_02_check_article_price(self):
        article_page = ArticleSubPage(self.ef_driver)
        self.ef_driver.get(article_page.URL)

        expected_price = 'PLN23.52'
        article_price = ArtSubPageLocators.XPATH_ARTICLE_PRICE

        self.assert_element_text(article_price, expected_price)

    @screenshot_decorator
    def test_03_product_added_to_basket(self):
        articles_page = ArtPage(self.ef_driver)
        self.ef_driver.get(articles_page.URL)

        expected_modal_text = '\ue876Product successfully added to your shopping cart'
        item_xpath = ArtPageLocators.XPATH_MOUNTAIN_FOX
        shopping_cart_btn_xpath = ArtPageLocators.XPATH_BTN_ADD_TO_CHART
        confirmation_modal_title_xpath = ArtPageLocators.XPATH_MODAL_TITLE

        articles_page.find_and_click_by_xpath(item_xpath)
        button = self.ef_driver.find_element_by_xpath(shopping_cart_btn_xpath)
        button.click()

        confirmation_modal_element = oh.visibility_of_element_wait(self.ef_driver,
                                                                   'xpath', confirmation_modal_title_xpath, 1)

        self.assertEqual(expected_modal_text, confirmation_modal_element.text)
        self.assertIn(expected_modal_text, confirmation_modal_element.text)


if __name__ == '__main__':
    unittest.main()
