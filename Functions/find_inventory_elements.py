from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

def find_inventory_elements(driver, max_retries=3, timeout=30):
    """
    Finds all inventory elements using multiple strategies and returns them in an array.

    Args:
    driver (WebDriver): The Selenium WebDriver instance.
    max_retries (int): Maximum number of retries for finding elements.
    timeout (int): Maximum wait time for elements to be present.

    Returns:
    list: A list of dictionaries, each containing 'name', 'xpath', and 'quantity' for an inventory item.
    """
    inventory_items = []
    strategies = [
        ("//button[contains(@class, 'item')]", ".//img", ".//*[contains(@class, 'amount') or contains(@class, 'quantity')]"),
        ("//div[contains(@class, 'item')]", ".//img", ".//*[contains(@class, 'amount') or contains(@class, 'quantity')]"),
        ("//*[contains(@class, 'inventory-item')]", ".//img", ".//*[contains(@class, 'amount') or contains(@class, 'quantity')]")
    ]

    for attempt in range(max_retries):
        for base_xpath, img_xpath, quantity_xpath in strategies:
            try:
                # Wait for the inventory items to be present
                WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.XPATH, base_xpath))
                )
                
                # Find all inventory items
                items = driver.find_elements(By.XPATH, base_xpath)

                for i, item in enumerate(items, 1):
                    try:
                        # Find the image element
                        img_element = item.find_element(By.XPATH, img_xpath)
                        
                        # Extract the item name from the image source
                        src = img_element.get_attribute("src")
                        item_name = src.split("/")[-1].split(".")[0]
                        
                        # Find the quantity element
                        quantity_element = item.find_element(By.XPATH, quantity_xpath)
                        quantity = quantity_element.text
                        
                        inventory_items.append({
                            "name": item_name,
                            "xpath": f"({base_xpath})[{i}]",
                            "quantity": quantity
                        })
                    
                    except (NoSuchElementException, StaleElementReferenceException) as e:
                        print(f"Error processing item {i}: {str(e)}")

                if inventory_items:
                    return inventory_items
            
            except TimeoutException:
                print(f"Timeout waiting for items with xpath: {base_xpath}")
            
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")

    print("Failed")
    return inventory_items