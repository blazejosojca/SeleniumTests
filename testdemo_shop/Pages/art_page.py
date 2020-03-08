from .base_page import BasePage


class ArtPage(BasePage):
    URL = 'https://autodemo.testoneo.com/en/9-art'
    TITLE = 'Art'

    def find_article_name(self, article):
        xpath = ("//a[contains(text(), '{0}')]/@href").format(article)
        element = self.driver.find_element_by_xpath(xpath)
        return element

    def find_and_click_by_article(self, article):
        xpath = ("//a[contains(text(), '{0}')]/@href").format(article)
        element = self.driver.find_element_by_xpath(xpath)
        element.click()
