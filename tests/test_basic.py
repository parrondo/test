
import test
import unittest


class BasicTestCase(unittest.TestCase):
    """ Basic test cases """

    def test_basic(self):
        """ check True is True """
        self.assertTrue(True)

    def test_version(self):
        """ check test exposes a version attribute """
        self.assertTrue(hasattr(test, "__version__"))
        self.assertIsInstance(test.__version__, str)


if __name__ == "__main__":
    unittest.main()
