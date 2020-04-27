from unittest import TestSuite, TextTestRunner

from testdemo_shop.Tests.lost_hat_login_tests import LoginTests
from testdemo_shop.Tests.lost_hat_sanity_tests import SanityPageTests


def sanity_test():
    test_suite = TestSuite()
    test_suite.addTest(LoginTests('test_03_check_login_to_registered_account'))
    test_suite.addTest(SanityPageTests('test_01_check_login_to_registered_account'))
    test_suite.addTest(SanityPageTests('test_02_check_search_engine'))
    test_suite.addTest(SanityPageTests('test_03_check_currency_of_products'))
    return test_suite


runner = TextTestRunner(verbosity=2)
runner.run(sanity_test())

