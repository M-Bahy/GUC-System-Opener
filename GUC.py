from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import threading

with open('env.txt', 'r') as file:
    Environment_Variables = file.read()
Environment_Variables = Environment_Variables.split('\n')
username = Environment_Variables[0]
password = Environment_Variables[1]
chrome_path = Environment_Variables[2]
mail = "https://mail.guc.edu.eg/owa/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2fmail.guc.edu.eg%2fowa%2f"
cms = "cms.guc.edu.eg/apps/student/HomePageStn.aspx"
portal = "apps.guc.edu.eg/student_ext/Console.aspx"

def open_mail(mail, username, password, driver):
    driver.get(mail)  
    username_field = driver.find_element(By.NAME, 'username')  
    password_field = driver.find_element(By.NAME, 'password')
    print(username_field)
    print(password_field)
    if username and password:
        username_field.send_keys(username)
        password_field.send_keys(password)  
        password_field.send_keys(Keys.RETURN)
    
        
def open_cms(driver):
    script = "window.open('{newTab}', '_blank');".format(newTab=f"https://{username}:{password}@{cms}")
    driver.execute_script(script)
    driver.switch_to.window(driver.window_handles[-1])

def open_portal(driver):
    script = "window.open('{newTab}', '_blank');".format(newTab=f"https://{username}:{password}@{portal}")
    driver.execute_script(script)
    driver.switch_to.window(driver.window_handles[-1])
        
chrome_options = Options()

chrome_options.binary_location = chrome_path
driver = webdriver.Chrome( options=chrome_options)
t1 = threading.Thread(target=open_mail, args=(mail, username, password, driver,))
t2 = threading.Thread(target=open_cms, args=(driver,))
t3 = threading.Thread(target=open_portal, args=(driver,))
t1.start()
t1.join()
t2.start()
t3.start()
t2.join()
t3.join()
while True :
    if not any(tab for tab in driver.window_handles if tab):
        driver.quit()
        break