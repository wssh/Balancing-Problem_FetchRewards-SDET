from selenium import webdriver
from balanceMethods import *

def setUp():
    driver = webdriver.Chrome()
    driver.get("http://ec2-54-208-152-154.compute-1.amazonaws.com/")
    assert "React App" in driver.title
    return driver


def secondWeigh(num1, num2, driver):
    fillLeftBox(0, num1, driver)
    fillRightBox(0, num2, driver)
    clickWeigh(driver)
    return getResult(driver)


def finalThree(num1, num2, num3, result, driver):
    if result == "=":
        print("The fake is bar #" + str(num3))
        clickBottomBar(num3, driver)
    elif result == "<":
        print("The fake is bar #" + str(num1))
        clickBottomBar(num1, driver)
    else:
        print("The fake is bar #" + str(num2))
        clickBottomBar(num2, driver)

def findFake():
    driver = setUp()
    # this algorithm will divide the bars into 3 sets. this will guarantee that we will find the fake bar in 2 weighs.
    # dividing the bars into 2 sets can give you a slight chance of finding the fake in 1 weigh. though we risk
    # finding the fake bar in 3 weighs instead

    # fill the bowls with [0,1,2] and [3,4,5]
    for i in range(0, 3):
        fillLeftBox(i, i, driver)
        fillRightBox(i, i + 3, driver)

    clickWeigh(driver)
    result = getResult(driver)
    clickReset(driver)

    if result == "=":  # if [0,1,2] and [3,4,5] are equal, then we know [6,7,8] houses the fake
        result = secondWeigh(6, 7, driver)
        finalThree(6, 7, 8, result, driver)

    elif result == ">":  # if [0,1,2] > [3,4,5], then we know [3,4,5] houses the fake
        result = secondWeigh(3, 4, driver)
        finalThree(3, 4, 5, result, driver)

    else:  # if [0,1,2] < [3,4,5], then we know [0,1,2] houses the fake
        result = secondWeigh(0, 1, driver)
        finalThree(0, 1, 2, result, driver)

    print("Total Weighs:")
    getWeighings(driver)
    driver.close()
