from unittest import TestSuite, TextTestRunner, TestLoader
from unittest.loader import makeSuite

from testdemo_shop.Tests.lost_hat_login_tests import LoginTests

def sanity_test():
    test_suite = TestSuite()
    test_suite.addTest(LoginTests('test_03_check_login_to_registered_account'))
    return test_suite

runner = TextTestRunner(verbosity=2)
runner.run(sanity_test())

