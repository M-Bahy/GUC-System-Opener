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
from dotenv import load_dotenv

load_dotenv()
chrome_path = os.getenv('chrome_path') 
Alive_time = os.getenv('aliveTime')
mail = os.getenv('mail')
cms = os.getenv('cms')
portal = os.getenv('portal')
username = os.getenv('username')
password = os.getenv('password')

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
if chrome_path:
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
if Alive_time:
    time.sleep(int(Alive_time))

driver.quit()
