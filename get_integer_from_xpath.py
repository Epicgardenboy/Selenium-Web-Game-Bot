from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def get_integer_from_xpath(driver, xpath, timeout=10):
    """
    Finds an element by XPath, extracts its text value, and returns it as an integer.
    
    Args:
    driver (WebDriver): The Selenium WebDriver instance.
    xpath (str): The XPath of the element.
    timeout (int): Maximum time to wait for the element (default is 10 seconds).
    
    Returns:
    int: The integer value extracted from the element's text.
    None: If the element is not found or the text cannot be converted to an integer.
    """
    # Wait for the element to be present
    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
        
    # Get the text content of the element
    text_value = element.text.strip()
        
    # Try to convert the text to an integer
    integer_value = int(text_value)
        
    return integer_value