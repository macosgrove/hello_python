# Import the 'unittest' module for running unit tests.
import unittest

# Check if the script is run as the main program.
if __name__ == '__main__':
    # Run the test cases using 'unittest.main()'.
    loader = unittest.TestLoader()
    start_dir = 'test'
    suite = loader.discover(start_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)