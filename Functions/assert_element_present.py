from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def assert_element_present(driver, xpath, timeout=10):
    """
    Asserts that an element specified by the given XPath is present on the page.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        xpath (str): The XPath locator for the element to be checked.
        timeout (int, optional): The maximum time to wait for the element to be present, in seconds. Default is 10 seconds.

    Raises:
        AssertionError: If the element is not present within the specified timeout.

    Example Usage:
        assert_element_present(driver, "/html/body/app-component/nav-component/div[2]/div[2]/button[10]")
    """
    try:
        wait = WebDriverWait(driver, timeout)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        raise AssertionError(f"Element with XPath '{xpath}' not found on the page within {timeout} seconds.")