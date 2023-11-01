import unittest

import util


class TestUtil(unittest.TestCase):

    def test_getyear(self):
        self.assertEqual(2023, util.getyear())

    @unittest.skip("demonstrating skipping")
    def test_getmonth(self):
        self.assertEqual(11, util.getmonth())

    def test_getday(self):
        self.assertNotEqual(0, util.getday())
