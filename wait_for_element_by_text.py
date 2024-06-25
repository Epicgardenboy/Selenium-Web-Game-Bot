from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def wait_for_element_by_text(driver, text, timeout=10):
    """
    Waits for an element containing the specified text to be present on the page.
    
    Args:
    driver (WebDriver): The Selenium WebDriver instance.
    text (str): The text to search for in the element.
    timeout (int): Maximum time to wait for the element (default is 10 seconds).
    
    Returns:
    WebElement: The found element if successful, None otherwise.
    """
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]"))
        )
        return element
    except TimeoutException:
        return None