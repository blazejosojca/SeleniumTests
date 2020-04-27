from unittest import TestSuite, TextTestRunner

from testdemo_shop.Tests.testoneo_smoke_shop_tests import SmokePagesTests


def smoke_suite():
    test_suite = TestSuite()
    test_suite.addTest(SmokePagesTests('test_01_title_main_page'))
    test_suite.addTest(SmokePagesTests('test_02_title_art_page'))
    test_suite.addTest(SmokePagesTests('test_03_title_clothes_page'))
    test_suite.addTest(SmokePagesTests('test_04_title_accessories_page'))
    test_suite.addTest(SmokePagesTests('test_05_title_login_page'))
    test_suite.addTest(SmokePagesTests('test_06_search_engine_return_list_of_products'))
    test_suite.addTest(SmokePagesTests('test_07_contact_form_is_displayed'))
    return test_suite


runner = TextTestRunner(verbosity=2)
runner.run(smoke_suite())
