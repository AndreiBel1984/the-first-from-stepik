from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)#1

wait = WebDriverWait(browser, 20)
element = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))#2

button = browser.find_element(By.XPATH,"//button[@id='book']")
button.click()#3

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text#4

y = calc(x)#4

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)#4

button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()#4
