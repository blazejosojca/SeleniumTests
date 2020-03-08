from .base_page import BasePage


class ArticleSubPage(BasePage):
    URL = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'

    def find_article_name(self, article):
        xpath = ("//a[contains(text(), '{0}')]/@href").format(article)
        return self.driver.find_element_by_xpath(xpath)
