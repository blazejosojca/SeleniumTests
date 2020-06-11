import unittest

from testdemo_shop.BaseTest import BaseTestClass
from testdemo_shop.locators import HomePageLocators

from testdemo_shop.Pages import home_page
from testdemo_shop.Helpers.wrappers import screenshot_decorator



class LostHatFrontPageTests(BaseTestClass):

    @screenshot_decorator
    def test_01_check_displaying_slider(self):
        homepage = home_page.HomePage(self.ef_driver)
        homepage.driver.get(homepage.base_url)
        homepage_slider = homepage.driver.find_element_by_css_selector(HomePageLocators.CSS_SLIDER)

        self.assertTrue(homepage_slider)

    @screenshot_decorator
    def test_02_slider_minimum_size(self):
        expected_size = {
            "height": "",
            "width": ""
        }
        homepage = home_page.HomePage(self.ef_driver)
        homepage.driver.get(homepage.base_url)
        homepage_slider = homepage.driver.find_element_by_css_selector(HomePageLocators.CSS_SLIDER)
        if self.ef_driver.name == 'firefox':
            expected_size["height"] = 340.0
            expected_size["width"] = 1110.0
        elif self.ef_driver.name == 'chrome':
            expected_size["height"] = 340
            expected_size["width"] = 690

        with self.subTest('Element height'):
            self.assertLessEqual(expected_size["height"], homepage_slider.size["height"])

        with self.subTest('Element width'):
            self.assertLessEqual(expected_size["width"], homepage_slider.size["width"])

        self.assertLessEqual(expected_size["height"], homepage_slider.size["height"])
        self.assertLessEqual(expected_size["width"], homepage_slider.size["width"])

    @screenshot_decorator
    def test_03_check_slider_contains_number_of_slides(self):
        number_of_slides = 3
        homepage = home_page.HomePage(self.ef_driver)
        homepage.driver.get(homepage.base_url)
        slider_elements = homepage.driver.find_elements_by_css_selector(HomePageLocators.CSS_SLIDER_ELEMENTS)
        number_of_slider_elements = (len(slider_elements))
        self.assertEqual(number_of_slides, number_of_slider_elements)

    @screenshot_decorator
    def test_04_slides_have_required_title_text(self):
        homepage = home_page.HomePage(self.ef_driver)
        homepage.driver.get(homepage.base_url)
        slides_titles = homepage.driver.find_elements_by_css_selector(HomePageLocators.CSS_SLIDES_TITLES)
        expected_text = "sample"

        for slide in slides_titles:
            slide_text_lower = slide.get_attribute("textContent").lower()
            with self.subTest(slide_text_lower):
                self.assertIn(expected_text, slide_text_lower,
                              f"Slides doesn't have expected text")

    @screenshot_decorator
    def test_05_articles_required_number_on_page(self):
        homepage = home_page.HomePage(self.ef_driver)
        homepage.driver.get(homepage.base_url)
        articles_miniatures = homepage.driver.find_elements_by_css_selector(HomePageLocators.CSS_ARTICLE_MINIATURE)
        number_of_articles_on_homepage = len(articles_miniatures)
        self.assertEqual(number_of_articles_on_homepage, 8)


if __name__ == '__main__':
    unittest.main()
