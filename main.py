# Import the 'unittest' module for writing unit tests.
import unittest

def count_nineteen_five(list):
    count = {19:0, 5:0}
    count[19] = len([x for x in list if x == 19])
    count[5] = len([x for x in list if x == 5])
    return count

def check_nineteen_five(list):
    count = count_nineteen_five(list)
    return count[19] == 2 and count[5] >= 3

class PrimeNumberTestCase(unittest.TestCase):
    def test_count_nineteen_five(self):
        list = [19, 5, 5, 3, 19, 21, 19]
        self.assertTrue(count_nineteen_five(list) == {19: 3, 5: 2})
        self.assertTrue(count_nineteen_five([]) == {19: 0, 5: 0})

    # Define a test method 'test_non_prime_numbers' to test non-prime numbers.
    def test_check_nineteen_five(self):
        self.assertFalse(check_nineteen_five([]))
        self.assertTrue(check_nineteen_five([19, 19, 15, 5, 3, 5, 5, 2]))
        self.assertFalse(check_nineteen_five([19, 15, 15, 5, 3, 3, 5, 2]))
        self.assertTrue(check_nineteen_five([19, 19, 5, 5, 5, 5, 5]))

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    unittest.main()