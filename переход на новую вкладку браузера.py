import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)#1

button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()#2

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)#3

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text#4

y = calc(x)#4

input1 = browser.find_element(By.ID, 'answer')
input1.send_keys(y)#4

button = browser.find_element(By.XPATH, "//button[@type='submit']")
button.click()#4
