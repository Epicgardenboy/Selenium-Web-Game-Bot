from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def click_menu_item(driver, menu_text, timeout=10, max_retries=3):
    """
    Clicks on a menu item based on its text content.
    Args:
    driver (WebDriver): The Selenium WebDriver instance.
    menu_text (str): The exact text of the menu item to click.
    timeout (int): Maximum wait time for elements to be present.
    max_retries (int): Maximum number of retries for finding and clicking the menu item.
    """
    for attempt in range(max_retries):
        print(f"Attempt {attempt + 1} of {max_retries} to click '{menu_text}'")
        try:
            # Wait for any button to be present (adjust if there's a more specific container)
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "button"))
            )

            # Find all buttons
            buttons = driver.find_elements(By.TAG_NAME, "button")

            for button in buttons:
                # Check button text and text of any child elements
                button_text = button.text.strip().lower()
                if menu_text.lower() in button_text:
                    # If text matches, try to click the button
                    try:
                        button.click()
                        print(f"Successfully clicked on '{menu_text}'")
                        return True
                    except Exception as e:
                        print(f"Found button but couldn't click: {str(e)}")
                        continue

            print(f"Could not find clickable button with text '{menu_text}' on attempt {attempt + 1}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        # Wait before retrying
        time.sleep(2)

    print(f"Failed to click on '{menu_text}' after {max_retries} attempts")
    return False