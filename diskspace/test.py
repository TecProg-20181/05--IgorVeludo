import unittest
from diskspace import *


class Test(unittest.TestCase):

    def testing_bytes_to_readble(self):
        blocks = 224
        result = "112.00Kb"
        command = bytes_to_readable(blocks)
        self.assertEqual(command, result)
