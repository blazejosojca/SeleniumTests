from unittest import TestSuite, TextTestRunner, TestLoader
from unittest.loader import makeSuite

from testdemo_shop.Tests.testoneo_smoke_shop_tests import SmokeTests

def smoke_suite():
    test_suite = TestSuite()
    test_suite.addTest(makeSuite(SmokeTests))
    return test_suite

runner = TextTestRunner(verbosity=2)
runner.run(smoke_suite)

