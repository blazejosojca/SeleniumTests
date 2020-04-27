from unittest import TestSuite, TextTestRunner
from unittest import loader
import unittest


from testdemo_shop.Tests.testoneo_smoke_shop_tests import SmokePagesTests
from testdemo_shop.Tests.lost_hat_article_tests import ArticleTests
from testdemo_shop.Tests.lost_hat_front_page_tests import LostHatFrontPageTests
from testdemo_shop.Tests.lost_hat_login_tests import LoginTests
from testdemo_shop.Tests.lost_hat_sanity_tests import SanityPageTests


def total_suite():
    test_suite = TestSuite()
    test_suite.addTest(loader.makeSuite(SmokePagesTests))
    test_suite.addTest(loader.makeSuite(ArticleTests))
    test_suite.addTest(loader.makeSuite(LostHatFrontPageTests))
    test_suite.addTest(loader.makeSuite(LoginTests))
    test_suite.addTest(loader.makeSuite(SanityPageTests))
    return test_suite


if __name__ == '__main__':
    runner = TextTestRunner(verbosity=2)
    runner.run((total_suite()))
