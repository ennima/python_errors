import os
import unittest
from error_logger import ErrorLogger


class TestErrorLogger(unittest.TestCase):

    def test_should_be_print_error(self):
        err = ErrorLogger("Error.txt")
        try:
            raise Exception("Unknown Error on this code.")
        except Exception as e:
            error_text = err.get_error(e)
            print(error_text)
            self.assertEqual(type("str"), type(error_text))

    def test_should_save_error_log(self):
        log_file = "Error.txt"
        err = ErrorLogger(log_file)
        print("Running test 2")
        try:
            raise Exception("Another Error on this code.")
        except Exception as e:
            err.save(e)
            file_exists = os.path.exists(log_file)
            self.assertTrue(file_exists)

