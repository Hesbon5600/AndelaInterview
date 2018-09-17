#Test for Tripple check
import unittest
from tripleCheck import tripple_check
class TestTrippleCheck(unittest.TestCase):
   def test_trippleCheck(self):
       lst = [5,8,5,4,8,5,8]
       self.assertEqual(tripple_check(lst), 4)

            
if __name__ == "__main__":
    unittest.main() 