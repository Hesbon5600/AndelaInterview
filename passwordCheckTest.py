# Python test case for validation of password 
import unittest
from password import password_validate
class TestPassword(unittest.TestCase):
    def test_passTest(self):
        #Password with less that 6 characters
        password2 = ["gfE3@", "2#hfH"]
        self.assertEqual(password_validate(password2), False)

        #Password more than 12 characters
        password3 = ["ABd12nsknjhgvmfdg34@1", "ABd1hbKBKksghb234@1"]
        self.assertEqual(password_validate(password3), False)

        #Password without a lower case character
        password4 = ["JHJ3J#$E3@", "JHJVJ56@#"]
        self.assertEqual(password_validate(password4), False)
        
        #password without an uppercase character
        password5 = ["jhbkj234@1", "mnbmk1634@1"]
        self.assertEqual(password_validate(password5), False)

        #Password without a number
        password6 = ["gfjbkBBE@", "#hfjzgkjBH"]
        self.assertEqual(password_validate(password6), False)

        #Correct Password
        password = ["ABd1234@1", "KHd1234@2", "kjfhv"]
        self.assertEqual(password_validate(password), True)


if __name__ == "__main__":
    unittest.main()