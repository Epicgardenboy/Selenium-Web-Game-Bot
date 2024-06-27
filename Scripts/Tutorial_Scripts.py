from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import loginInfo
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time
from Functions.find_inventory_element_and_click import find_inventory_element_and_click
from Functions.find_inventory_elements import find_inventory_elements
from Functions.wait_and_type_element import wait_and_type_element
from Functions.wait_and_click_element import wait_and_click_element
from Functions.click_menu_item import click_menu_item
from Functions.wait_for_element_by_text import wait_for_element_by_text
from Functions.get_integer_from_xpath import get_integer_from_xpath



def tutorial_page_one(driver):
    # Tutorial Page One
    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Gather a Pine Log from Woodcutting")
    click_menu_item(driver, "Pine Log") # Fails a lot of the time but needed incase Pine Log is not selected already
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/skill-page/div/div[1]/button") # "Gather" defaults to gather potion so XPath to gather must be used
    time.sleep(10) # Action only takes 4.1 but accounting for bad connection
    click_menu_item(driver, "Stop & Loot")


    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Gather a Copper Ore from Mining")
    click_menu_item(driver, "Copper Rock")
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/skill-page/div/div[1]/button") # "Gather" defaults to gather potion so XPath to gather must be used
    time.sleep(10) # Action only takes 4.1 but accounting for bad connection
    click_menu_item(driver, "Stop & Loot")


    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Create Charcoal from Smelting by using the")
    click_menu_item(driver, "Charcoal")
    click_menu_item(driver, "Pine Log")
    click_menu_item(driver, "Max")
    click_menu_item(driver, "Create")


    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Craft a Copper Bar from Smelting")
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/skill-page/div/div[1]/div[3]/button[2]") # "Craft" defaults to craft potion so XPath to Craft mut be used
    time.sleep(10) # Action only takes 4.1 but accounting for bad connection

    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Claim")



def tutorial_page_two(driver):
    # Tutorial Page Two
    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Craft a Copper Sword from Forging")
    click_menu_item(driver, "Copper")
    click_menu_item(driver, "Copper Sword")
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/skill-page/div/div[1]/div[3]/button[2]") # "Craft" defaults to craft potion so XPath to Craft mut be used
    time.sleep(10) # Action only takes 4.1 but accounting for bad connection

    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Craft a Copper Shield from Smithing")
    click_menu_item(driver, "Copper")
    click_menu_item(driver, "Copper Shield")
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/skill-page/div/div[1]/div[3]/button[2]") # "Craft" defaults to craft potion so XPath to Craft mut be used
    time.sleep(10) # Action only takes 4.1 but accounting for bad connection
    click_menu_item(driver, "Stop & Loot") # Need to stop and loot this time so shield is available to equip

    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Go to the Equipment page")
    click_menu_item(driver, "Main Hand")
    click_menu_item(driver, "Copper Sword")
    click_menu_item(driver, "Off Hand")
    click_menu_item(driver, "Copper Shield")

    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Claim")



def tutorial_page_three(driver):
    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Craft 150 Copper Helmets from Smithing")
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/skill-page/div/div[1]/div[3]/button[2]") # "Craft" defaults to craft potion so XPath to Craft mut be used
    numHelmet = 0
    while numHelmet < 51:
        numHelmet = get_integer_from_xpath(driver, "/html/body/app-component/div/div/div/skill-page/div/div[1]/div[3]/div[2]/div[3]")
        time.sleep(1)
    click_menu_item(driver, "Stop & Loot") # Need to stop and loot this time so bars are not wasted

    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Go to the Inventory page")
    click_menu_item(driver, "Upgrade")
    find_inventory_element_and_click(driver, "helmet")
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/inventory-page/modal-component/div/div[2]/div/div/div[7]/div")
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/inventory-page/modal-component/div/div[2]/div/div/div[7]/div")
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/inventory-page/modal-component/div/div[2]/div/div/div[7]/div")
    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Claim")



def tutorial_page_four(driver):
    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Buy Seeds from the Merchant")
    click_menu_item(driver, "Seeds")
    wait_and_type_element(driver, "/html/body/app-component/div/div/div/merchant-page/div/div[2]/div/div[6]/input", "1")
    click_menu_item(driver, "Buy")

    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Gather Pine Logs from Woodcutting until an Apple drops")
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/skill-page/div/div[1]/button") # "Gather" defaults to gather potion so XPath to gather must be used
    while get_integer_from_xpath(driver, "/html/body/app-component/div/div/div/skill-page/div/div[1]/div[2]/div[3]/div[3]", timeout = 10000) < 1:
        time.sleep(1)
    click_menu_item(driver, "Stop & Loot")

    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Create Compost from Farming by using the")
    click_menu_item(driver, "Compost")
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/skill-page/compost-component/overlay-component/div/div/div/div/div[1]/div[2]/div[2]/button[8]") # Hardcoded because "Apple" does not seem to work
    wait_and_type_element(driver, "/html/body/app-component/div/div/div/skill-page/compost-component/overlay-component/div/div/div/div/div[2]/div/div[5]/input", "1")
    click_menu_item(driver, "Create")

    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Gather a Potato from Farming")
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/skill-page/div/div[1]/button") # "Gather" defaults to gather potion so XPath to gather must be used
    time.sleep(10)

    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Buy Fishing Bait from the Merchant")
    click_menu_item(driver, "Fishing Bait")
    wait_and_type_element(driver, "/html/body/app-component/div/div/div/merchant-page/div/div[2]/div/div[6]/input", "1")
    click_menu_item(driver, "Buy")

    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Gather a Raw Shrimp from Fishing")
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/skill-page/div/div[1]/button") # "Gather" defaults to gather potion so XPath to gather must be used
    time.sleep(10)

    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Craft a Shrimp Pie from Cooking")
    wait_and_click_element(driver, "/html/body/app-component/div/div/div/skill-page/div/div[1]/div[3]/button[2]") # "Craft" defaults to gather potion so XPath to gather must be used
    time.sleep(10)

    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Claim")



def tutorial_page_five_and_six(driver):
    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Go to the Equipment page")
    click_menu_item(driver, "Food")
    click_menu_item(driver, "Shrimp Pie")
    click_menu_item(driver, "All")
    click_menu_item(driver, "Equip")
    click_menu_item(driver, "Helmet")
    click_menu_item(driver, "Perfect Copper Helmet")

    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Defeat a Snake")
    click_menu_item(driver, "Fight")
    time.sleep(5)
    wait_for_element_by_text(driver, "Bone", timeout = 1000) # Getting the number of bones gathered would not work, I do not know why
    click_menu_item(driver, "Tutorial")
    click_menu_item(driver, "Claim")

    # Page 6 (extra rewards)
    time.sleep(3)
    click_menu_item(driver, "Claim")
