# End-to-End-Machine-Learning-Project

## exception.py File Explanation 

```python
import sys
```
This line imports the `sys` module, which provides access to system-specific parameters and functions.

```python
def error_message_details(error, error_detail: sys):
```
This line defines a function called `error_message_details` that takes two parameters: `error` and `error_detail`. The `error_detail` parameter has a type hint indicating that it should be of type `sys`.

```python
_, _, exc_tb = error_detail.exc_info()
```
This line calls the `exc_info()` method of the `error_detail` object, which is expected to be an instance of the `sys` module. The `exc_info()` method returns a tuple containing information about the current exception being handled. The line uses the tuple unpacking feature to assign the three elements of the tuple to the variables `_`, `_`, and `exc_tb`, respectively. The underscore `_` is commonly used as a throwaway variable to indicate that its value is not needed.

```python
file_name = exc_tb.tb_frame.f_code.co_filename
```
This line retrieves the file name where the error occurred from the traceback object `exc_tb`. The `tb_frame` attribute of the traceback object represents the frame where the error occurred. The `f_code` attribute of the frame object represents the code object associated with the frame. Finally, the `co_filename` attribute of the code object provides the file name.

```python
error_message = "Error Occurred in Python Script name [{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
```
This line creates an error message string using the file name, line number, and the error message passed to the function. It uses the `format()` method to insert the values of `file_name`, `exc_tb.tb_lineno`, and `str(error)` into the specified placeholders `{0}`, `{1}`, and `{2}`.

```python
return error_message
```
This line returns the generated error message from the function.

```python
class CustomException(Exception):
```
This line defines a custom exception class called `CustomException` that inherits from the built-in `Exception` class.

```python
def __init__(self, error_message, error_detail: sys):
```
This line defines the constructor method `__init__` for the `CustomException` class. It takes three parameters: `self` (representing the instance being created), `error_message`, and `error_detail`. The `error_detail` parameter has a type hint indicating that it should be of type `sys`.

```python
super().__init__(error_message)
```
This line calls the `__init__` method of the parent class (`Exception`) using the `super()` function. It initializes the exception object with the provided `error_message`.

```python
self.error_message = error_message_details(error_message, error_detail=error_detail)
```
This line assigns the value returned by the `error_message_details` function to the `self.error_message` attribute of the instance. The `error_message_details` function is called with the `error_message` and `error_detail` parameters.

```python
def __str__(self):
```
This line defines the `__str__` method for the `CustomException` class. The `__str__` method is a special method in Python that is automatically called when the instance is converted to a string, for example, when using the `str()` function or printing the instance.

```python
return self.error_message
```
This line returns the error message stored in the `self.error_message` attribute.


## logger.py File Explanation 

```python
import logging
import os
from datetime import datetime
```
- This section imports the necessary modules: `logging` for logging functionality, `os` for working with file paths and directories, and `datetime` for generating timestamps.

```python
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
```
- This line creates a timestamped log file name using the current date and time. The `datetime.now()` function returns the current date and time, and `strftime('%m_%d_%Y_%H_%M_%S')` formats it as "month_day_year_hour_minute_second". The `.log` extension is appended to the file name.

```python
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)
```
- Here, `logs_path` is created by joining the current working directory (`os.getcwd()`), the "logs" folder, and the `LOG_FILE` name. The `os.makedirs()` function is used to create the necessary directories if they don't exist, with the `exist_ok=True` parameter ensuring that no exception is raised if the directories already exist.

```python
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
```
- This line creates the full path to the log file by joining `logs_path` and `LOG_FILE`.

```python
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
```
- Here, the logging configuration is set up using `basicConfig()` from the `logging` module. The `filename` parameter specifies the log file path. The `format` parameter sets the format for the log messages, including the timestamp (`%(asctime)s`), line number (`%(lineno)d`), logger name (`%(name)s`), log level (`%(levelname)s`), and the actual log message (`%(message)s`). The `level` parameter sets the logging level to `INFO`, which means that log messages with severity level `INFO` and above will be recorded in the log file.

```python
# if __name__ == "__main__":
#     logging.info("Logging has Started")
```
- These lines are commented out in the code snippet. If uncommented, they would log the message "Logging has Started" with the `INFO` level when the script is directly executed, indicating that the logging process has begun.