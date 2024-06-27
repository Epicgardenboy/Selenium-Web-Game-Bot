from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

def find_inventory_element_and_click(driver, image_filename, timeout=100):
    """
    Finds the button in the inventory page containing the specified image, and then clicks on the button.

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        image_filename (str): The filename or unique part of the image source. e.g. "gem-ruby.png"
        timeout (int, optional): The maximum time to wait for the element to be present, in seconds. Default is 100 seconds.

    Returns:
        bool: True if the button was found and clicked, False otherwise.
    """
    # XPath to find the button containing the image
    xpath = f"//button[.//img[contains(@src, '{image_filename}')]]"

    try:
        # Wait for the button to be present
        button = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        
        print(f"Button found: {button.get_attribute('outerHTML')}")

        # Scroll the button into view
        driver.execute_script("arguments[0].scrollIntoView(true);", button)

        # Wait a short time after scrolling
        time.sleep(1)

        # Try different click methods
        try:
            button.click()
        except ElementClickInterceptedException:
            print("Normal click failed, trying JavaScript click.")
            driver.execute_script("arguments[0].click();", button)

        print(f"Successfully clicked button containing image: {image_filename}")
        return True

    except TimeoutException:
        print(f"Timeout: Button with image {image_filename} not found within {timeout} seconds.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    return False

# Example usage:
# find_inventory_element_and_click(driver, image_filename="gem-ruby.png")