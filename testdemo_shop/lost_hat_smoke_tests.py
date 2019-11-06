import unittest
from BaseTest import MainTest
from testdemo_shop.locators import (LoginPageLocators,
                                    AccountPageLocators,
                                    ArticlesPageLocators,
                                    HomePageLocators)
from testdemo_shop.pages import (LoginPage,
                                 AccountPage,
                                 ArticlePage,
                                 HomePage,
                                 ArtPage,
                                 ClothesPage,
                                 AccessoriesPage)
from testdemo_shop.helpers.functional_helper import user_login

from Configuration import Config


class SmokeTests(MainTest):

    def test_01_title_main_page(self):
        homepage = HomePage(self.driver)
        homepage.driver.get(homepage.base_url)
        home_title = homepage.driver.title
        self.assertEqual(HomePage._home_title, home_title)

    def test_02_title_art_page(self):
        art_page = ArtPage(self.driver)
        art_page.driver.get(art_page.art_url)
        art_title = art_page.driver.title
        self.assertEqual(ArtPage._art_title, art_title)


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
