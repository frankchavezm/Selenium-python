
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#https://www.geeksforgeeks.org/selenium-python-tutorial/

def waitForElement(wait, by, value):
    wait.until(EC.visibility_of_element_located((by, value)))

def clickElement(driver, by, value):
    element = driver.find_element(by, value)
    element.click()

def sendText(driver, by, value, text):
    element = driver.find_element(by, value)
    element.send_keys(text)

def getText(driver, by, value):
    element = driver.find_element(by, value)
    return element.text

def delay(driver,seconds):
    driver.implicitly_wait(seconds)

ISSUE_DESCRIPTION = 'The filer that hosts my web site is not working'
TIME_OUT= 100
driver = webdriver.Chrome()
wait = WebDriverWait(driver, TIME_OUT)


driver.get("https://gf-docs-demo.s3.us-south.cloud-object-storage.appdomain.cloud/netapp-WAC.html")

#launcher
waitForElement(wait, By.ID, "WACLauncher__Button")
clickElement(driver, By.ID, "WACLauncher__Button")

#Select the 1st option
waitForElement(wait, By.XPATH, "//*[@id='WACHomeScreen__starter-0']")
clickElement(driver, By.XPATH, "//*[@id='WACHomeScreen__starter-0']")


#Wait for the input form
waitForElement(wait, By.XPATH, "//*[@id='I’d be happy to help, please describe your issue and how long you’ve experienced this issue']")

#Enter issue description
sendText(driver, By.XPATH, "//*[@id='I’d be happy to help, please describe your issue and how long you’ve experienced this issue']", ISSUE_DESCRIPTION)
clickElement(driver, By.XPATH, "//button[text()='Submit']")

#Wait for the next screen
waitForElement(wait,By.XPATH,"//*[@id='WAC__message-1']/div[3]/div/div/div/div/main/div[2]/div/div/div/div/div/div[2]/form/div/div[1]/div/div/span[2]/p/div/span")
delay(driver,2)
clickElement(driver, By.XPATH, "//button[text()='Submit']")


#wait for table
waitForElement(wait, By.XPATH, "//*[@id='WAC__message-1']/div[3]/div/div/div/div/main/div[3]/div/div/div/div/div/div[2]/form/div/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label")
delay(driver,2)
#Select 1st row in table
clickElement(driver, By.XPATH, "//*[@id='WAC__message-1']/div[3]/div/div/div/div/main/div[3]/div/div/div/div/div/div[2]/form/div/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]")

clickElement(driver, By.XPATH, "//button[text()='Submit']")

#wait for next screen
waitForElement(wait, By.XPATH, "//*[@id='WAC__message-1']/div[3]/div/div/div/div/main/div[4]/div/div/div/div/div/div[2]/form/div/div[1]/div/div/span[2]/p/div")
#Click Submit
clickElement(driver, By.XPATH, "//button[text()='Submit']")

#wait for next screen
waitForElement(wait, By.XPATH, "//*[@id='WAC__message-1']/div[3]/div/div/div/div/main/div[5]/div/div/div/div/div/div[1]")

delay(driver,3)

#Enter impact for users
sendText(driver, By.XPATH, "//*[@id='impact']","impact")

#Enter whan was observed
sendText(driver, By.XPATH, "//*[@id='when_observed']","yesterday")

#Enter recent changes
sendText(driver, By.XPATH, "//*[@id='recent_changes_maintenance']","recent changes")

delay(driver,3)

#Click Submit
clickElement(driver, By.XPATH, "//button[text()='Submit']")

#wait for next screen
waitForElement(wait, By.XPATH, "//*[@id='WAC__message-1']/div[3]/div/div/div/div/main/div[6]/div/div/div/div/div/div[2]/form/div/div[1]/div/div/span[2]/p/div/span")

#Click Submit
clickElement(driver, By.XPATH, "//button[text()='Submit']")

#wait for next screen
waitForElement(wait, By.XPATH, "//*[@id='WAC__message-1']/div[3]/div/div/div/div/main/div[7]/div/div/div/div/div/div[2]/form/div/div[16]/div/div/span[2]/p/div")

#Click Submit
clickElement(driver, By.XPATH, "//button[text()='Submit']")


#wait for next screen
waitForElement(wait, By.XPATH, "//*[@id='WAC__message-1']/div[3]/div/div/div/div/main/div[8]/div/div/div/div/div/div[2]/form/div/div[2]/div/div/span[2]/p/div")

result = getText(driver, By.XPATH, "//*[@id='WAC__message-1']/div[3]/div/div/div/div/main/div[8]/div/div/div/div/div/div[2]/form/div/div[2]/div/div/span[2]/p/div")
#print(result)
# Asserting that the expected title fragment is present in the actual text 

assert ("Thank you. You’ve successfully created a " in result) 

#Click Submit
clickElement(driver, By.XPATH, "//button[text()='Submit']")

driver.get_screenshot_as_file('wxo.png') 
driver.quit()