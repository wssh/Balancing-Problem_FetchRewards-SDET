from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def getResult(driver):
    result = driver.find_element_by_class_name("result").find_element_by_id("reset")
    return result.text


def fillLeftBox(box, number, driver):
    left = "left_" + str(box)
    driver.find_element_by_id(left).send_keys(number)


def fillRightBox(box, number, driver):
    right = "right_" + str(box)
    driver.find_element_by_id(right).send_keys(number)


def clickWeigh(driver):
    driver.find_element_by_id("weigh").click()
    WebDriverWait(driver, 10).until(lambda wait: getResult(driver) != "?")


def clickReset(driver):
    resets = driver.find_elements_by_id("reset")
    resets[1].click()


def getWeighings(driver):
    infoClass = driver.find_element_by_class_name("game-info")
    infoList = infoClass.find_elements_by_tag_name("li")
    for li in infoList:
        print(li.text)


def clickBottomBar(number, driver):
    bar = "coin_" + str(number)
    driver.find_element_by_id(bar).click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    a = Alert(driver)
    assert "Yay! You find it!" in a.text
    print (a.text)
    a.dismiss()
