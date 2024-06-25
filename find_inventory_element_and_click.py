from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def find_inventory_element_and_click(driver, source, timeout = 100):
    """
    Finds the element in the inventory page, and then clicks on the element

    Args:
        driver (WebDriver): The Selenium WebDriver instance.
        source (str): The source of the image to be located. e.g. ".//img[@src='/assets/items/gem-ruby.png']"
        timeout (int, optional): The maximum time to wait for the element to be present, in seconds. Default is 10 seconds.

    Example Usage: 
    find_inventory_element_and_click(driver, source = ".//img[@src='/assets/items/gem-ruby.png']")
    
    """
    # Assuming the webpage is already loaded
    base_xpath = "/html/body/app-component/div/div/div/inventory-page/div/div[1]/div/div[3]/button["
    found = False

    for i in range(1, timeout + 1):
        # Construct the full XPath for each button
        full_xpath = base_xpath + str(i) + "]"

        try:
            # Find the button element
            element = driver.find_element(By.XPATH, full_xpath)

            # Check if the button contains the Ruby image
            image = element.find_element(By.XPATH, source)
            element.click()
        except NoSuchElementException:
            filler = 1+1
        else:
            found = True

        # Stop after max_items even if desired item not found
        if i == timeout or found == True:
            break