from unittest import TestSuite, TextTestRunner
from unittest.loader import makeSuite

from testdemo_shop.Tests.testoneo_smoke_shop_tests import SmokeTests
from testdemo_shop.Tests.lost_hat_article_tests import ArticleTests
from testdemo_shop.Tests.lost_hat_front_page_tests import LostHatFrontPageTests
from testdemo_shop.Tests.lost_hat_login_tests import LoginTests


def total_suite():
    test_suite = TestSuite()
    test_suite.addTest(makeSuite(SmokeTests))
    test_suite.addTest(makeSuite(ArticleTests))
    test_suite.addTest(makeSuite(LostHatFrontPageTests))
    test_suite.addTest(makeSuite(LoginTests))
    return test_suite

if __name__ == '__main__':
    runner = TextTestRunner(verbosity=2)
    runner.run((total_suite()))
