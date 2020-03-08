from unittest import TestSuite, TextTestRunner, TestLoader
from testdemo_shop.Tests.testoneo_smoke_shop_tests import SmokePagesTests

def smoke_suite():
    test_suite = TestSuite()
    test_suite.addTest(unittest.makeSuite(SmokePagesTests))
    return test_suite

runner = TextTestRunner(verbosity=2)
runner.run(smoke_suite())
