import unittest
from BaseTest import MainTest
from testdemo_shop.Pages import article_sub_page
from testdemo_shop.locators import ArticlesPageLocators
from testdemo_shop.Helpers.wrappers import screenshot_decorator

class ArticleTests(MainTest):

    @screenshot_decorator
    def test_01_check_article_name(self):
        article_page = article_sub_page.ArticleSubPage(self.ef_driver)
        self.ef_driver.get(article_page.URL)
        expected_name = 'HUMMINGBIRD PRINTED T-SHIRT'
        self.assert_element_text(ArticlesPageLocators.XPATH_ARTICLE_NAME, expected_name)

    @screenshot_decorator
    def test_02_check_article_price(self):
        article_page = article_sub_page.ArticleSubPage(self.ef_driver)
        self.ef_driver.get(article_page.URL)
        expected_price = 'PLN23.52'
        self.assert_element_text(ArticlesPageLocators.XPATH_ARTICLE_PRICE, expected_price)


if __name__ == '__main__':
    unittest.main()
