import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
username = "enter username"
access_key = "enter access key"
grid_Url = "hub.lambdatest.com/wd/hub"
options = webdriver.ChromeOptions()
options.browser_version = ""
options.platform_name = "Windows 11"
lt_options = {}
lt_options["username"] =""
lt_options["accessKey"] ="MHu1nfiZVVPSteHsFVqybmvsxePoFJq0j8htKDk7uHcRwPgLGg"
lt_options["project"] = "Parallel1"
lt_options["selenium_version"] = "4.0.0"
lt_options["w3c"] = True
options.set_capability('LT:Options', lt_options)
# lt_options = {}
url = "https://"+username+":"+access_key+"@"+grid_Url
driver = webdriver.Remote(
    command_executor=url,
    options=options
    )
driver.get("https://accounts.lambdatest.com/")
# driver.get("https://accounts.lambdatest.com/")
u_name = driver.find_element("id", "email")
u_name.send_keys("enter emaik address")

# for  password
p_word = driver.find_element("id", "password")
p_word.send_keys("enter password")
# for login
login = driver.find_element("id", "login-button")
login.send_keys(Keys.ENTER)
time.sleep(10)
# for dropdown
print("Test completed")
time.sleep(10)
driver.quit()
