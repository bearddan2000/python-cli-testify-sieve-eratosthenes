from testify import *
from io import StringIO
from unittest.mock import patch
import unittest

import main

class TestMain(TestCase):
    """docstring for TestMain."""
    def test_SieveOfEratosthenes(self):
        with patch('sys.stdout', new = StringIO()) as captured:
            main.SieveOfEratosthenes(2)
            assert_equal(captured.getvalue(), "2\n")

if __name__ == '__main__':
    run()
