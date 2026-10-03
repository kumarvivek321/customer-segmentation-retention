import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Captures file name and line number where the exception occurred.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    """
    Custom exception that inherits from Python's base Exception class.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0  # Deliberate division by zero to test our custom exception
    except Exception as e:
        logging.info("Divide by zero error triggered for testing.")
        raise CustomException(e, sys)
