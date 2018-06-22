import unittest
import subprocess
from diskspace import *


class Test(unittest.TestCase):

    def testing_bytes_to_readble(self):
        blocks = 224
        result = "112.00Kb"
        command = bytes_to_readable(blocks)
        self.assertEqual(command, result)

    def testing_subprocess_check_output(self):
        command = 'du'
        firstResult = subprocess.check_output(command.strip().split(' '))
        finalResult = subprocess_check_output(command)
        self.assertEqual(firstResult, finalResult)

if __name__ == '__main__':
    unittest.main()
