from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_type_element(driver, xpath, text, timeout=10):
    """
    Waits for an element specified by the given XPath to be present on the page,
    and then clicks the element.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        xpath (str): The XPath locator for the element to be typed in.
        text (str): The string to be typed in the textbox.
        timeout (int, optional): The maximum time to wait for the element to be present, in seconds. Default is 10 seconds.

    Example Usage:
    wait_and_click_element(driver, "/html/body/app-component/nav-component/div[2]/div[2]/button[10]", "This will be typed", max_wait_time=100)
    """

    wait = WebDriverWait(driver, timeout)
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    element.send_keys(text)