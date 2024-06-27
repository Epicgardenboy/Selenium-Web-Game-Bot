from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException

def get_integer_from_xpath(driver, xpath, timeout=100, default_value=None):
    """
    Finds an element by XPath, extracts its text value, and returns it as an integer.
    If the element is not found or the value cannot be converted to an integer,
    it returns the default value and continues execution.
    
    Args:
    driver (WebDriver): The Selenium WebDriver instance.
    xpath (str): The XPath of the element.
    timeout (int): Maximum time to wait for the element (default is 10 seconds).
    default_value (int, optional): The value to return if the element is not found or cannot be converted to an integer.
    
    Returns:
    int: The integer value extracted from the element's text, or the default value if not found/convertible.
    """
    try:
        # Wait for the element to be present
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        
        # Get the text content of the element
        text_value = element.text.strip()
        
        # Try to convert the text to an integer
        integer_value = int(text_value)
        
        print(f"Successfully extracted integer value: {integer_value}")
        return integer_value
    
    except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
        two=1+1
    except ValueError:
        print(f"Unable to convert '{text_value}' to an integer for XPath: {xpath}. Continuing with default value.")
    except Exception as e:
        print(f"An unexpected error occurred for XPath: {xpath}. Error: {str(e)}. Continuing with default value.")
    
