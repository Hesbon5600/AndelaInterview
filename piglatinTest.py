import unittest
from piglatin import pig_latin
class PiglatinTest(unittest.TestCase):
    def test_piglatin(self):
        string = "psd3sd?s?d?7sd?sd?s?d3s"
        self.assertEqual(pig_latin(string), True)

        string2 = "fh8?ilj?5jj?j??2"
        self.assertEqual(pig_latin(string2), False)

if __name__ == "__main__":
    unittest.main()

