from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from robot.api.deco import keyword
from selenium.common.exceptions import TimeoutException
from time import sleep

@keyword('Launch url')
def launch():
    chrome_driver_path = "C:\Selenium\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    url = "https://bt.com/"
    driver.get(url)
    driver.maximize_window()
    timer = 5
    while timer >=0:
        try:
            element = WebDriverWait(driver, 20) .until(EC.presence_of_element_located((By.XPATH, '//a[@class="call" and text()="Accept all cookies"]')))
            element.click()
            break
        except TimeoutException:
            sleep(1)
            timer = timer - 1
    else:
        raise Exception("failed to click on acept cookies")

@keyword('Hover to "${control1:[^"]+}" menu and From "${control2:[^"]+}" menu, select "${control3:[^"]+}"')
def mobile_menu(controlname1,controlname2,controlname3):
    mobile = '//span[text()="'+controlname1+'"]'
    element = findelement(None, locator=(By.XPATH, mobile))
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    sub_items = '(// a[text() = "'+controlname3+'"])[1]'
    timer = 5
    while timer >= 0:
        try:
            element2 = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, sub_items)))
            element2.click()
            break
        except TimeoutException:
            sleep(1)
            timer = timer - 1
    else:
        raise Exception(f"failed to click on subitem {controlname3}")


@keyword(' Verify the numbers of banners present below “See Handset details” should not be less than "${control3:[^"]+}"')
def count_of_banners(bannercount):
    bannerxpath ='//div[@class="flexpay-card_card_wrapper__Antym"]'
    timer = 5
    while timer >= 0:
        try:
            elements = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, bannerxpath)))
            break
        except TimeoutException:
            sleep(1)
            timer = timer - 1
    else:
        raise Exception("failed to get handle of banners")
    uibannercount= len(elements)
    print(f"The number of banner on ui is {len(elements)}")
    if uibannercount >=3:
        print("The number if banner present below is not less than 3")
    else:
        raise Exception(f"The number of banners on ui is {len(elements)} which doesnot match with user value {bannercount}")

@keyword('Scroll down and click View SIM only deals')
def scroll_to_sim():
    sim_xpath = '//a[text()="View SIM only deals"]'
    sim_locator =driver.find_element(By.XPATH, sim_xpath)
    timer = 5
    while timer >= 0:
        try:
            driver.execute_script("arguments[0].scrollIntoView();", sim_locator)
            break
        except TimeoutException:
            sleep(1)
            timer = timer - 1
    else:
        raise Exception("failed to scroll down")
    sim_locator.click()
    print("click on view sim only ")

@keyword('Validate the title for new page.')
def validate_title():
    title = driver.title
    if title.lower() == 'simonlydeals|comparesimoplans&contracts|btmobile':
        print("Validate title")
    else:
        raise Exception("The url doesn't seem to be validate")

@keyword('Validate "${control1:[^"]+}"')
def validate_title(str):
    strcontrol = '//div[@class="banner-ee-promo_text_inner_container__1nJie"]/h2'
    timer = 5
    while timer >= 0:
        try:
            element3 = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, strcontrol)))
            uistr = element3.text()
            break
        except TimeoutException:
            sleep(1)
            timer = timer - 1
    else:
        raise Exception(f"failed to click on subitem {controlname3}")
    if str == uistr:
        print("validate string")
    else:
        raise Exception(f"Excepted string is {str} byt actual string is {uistr}")

@keyword('Close the browser & exit')
def close_browser():
    driver.close()