import sys 


def error_message_details(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    # exc_tb holds the values or information about the line or occurance of the Error and all the things

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error Occured in Python Script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message