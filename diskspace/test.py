import unittest
import subprocess
from diskspace import *


class Test(unittest.TestCase):

    def test_bytes_to_readable_Bits(self):
        function = bytes_to_readable(1)
        self.assertEquals('512.00B', function)

    def test_bytes_to_readable_Kb(self):
        function = bytes_to_readable(1024)
        self.assertEquals('512.00Kb', function)

    def test_subprocess_check_output(self):
        command = 'du'
        firstResult = subprocess.check_output(command.strip().split(' '))
        finalResult = subprocess_check_output(command)
        self.assertEqual(firstResult, finalResult)

    def test_show_space_list(self):
        self.assertIsNone(show_space_list(directory='.', depth=-1, order=True))

if __name__ == '__main__':
    unittest.main()
