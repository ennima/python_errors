import sys
from datetime import datetime


class ErrorLogger:
    """
    This class make an error message with time of error, type, file and line.
    This class can save the formatted errors to a file.

    :file is the name of log error file

    Usage:

    # Declaring the err object
    err = ErrorLogger('ERROR.txt')

    # Catching error and save the log
    try:
        raise Exception('Some error')
    except Exception as e:
        err.save(e)

    """

    def __init__(self, file: str):
        self.file = file

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, value):
        if type(value) == type("string"):
            self.__file = value
        else:
            raise Exception(f"ValueError: File should be an str not {type(value).__name__}")

    def get_error(self, e: Exception):
        """
        Return a text with the error log.

        :param e: Exception - Is the exception catched
        :return: str
        """
        exc_type, exc_obj, exc_tb = sys.exc_info()
        now_time = datetime.now()
        return f"""------- [{now_time}]:
        File: {__file__}
        [Error: {exc_type.__name__}]: {e} 
        Line: {exc_tb.tb_lineno}"""

    def save(self, e):
        """
        Append error log data to a log file.

        :param e: Exception - Is the exception catched
        :return: None
        """
        exc_type, exc_obj, exc_tb = sys.exc_info()
        now_time = datetime.now()
        error_text = f"""------- [{now_time}]:
        File: {__file__}
        [Error: {exc_type.__name__}]: {e} 
        Line: {exc_tb.tb_lineno}

"""
        with open(self.__file, "a") as file:
            file.write(error_text)
