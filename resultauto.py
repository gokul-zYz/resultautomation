from selenium import webdriver 
import http.client
import time
import os
import chromedriver_autoinstaller


chromedriver_autoinstaller.install()
driver=webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

def whatsapp():
  
  
   payload = "token=zi2hk1ie8vevmc3m&to=+919360686061&body=gokul&priority=1&referenceId="
   headers = { 'content-type': "application/x-www-form-urlencoded" }
   conn.request("POST", "/instance21482/messages/chat", payload, headers)
   

def results():
 
 
 driver.get("http://exam.pondiuni.edu.in/results/")
 const="19TH0426"

 driver.find_element_by_xpath('//*[@id="reg_no"]').send_keys(const)
 driver.find_element_by_xpath('//*[@id="exam"]').send_keys("sixth")
 driver.find_element_by_xpath('//*[@id="print_app_form"]/span').click()
 time.sleep(1)
 
  
 try:
  driver.switch_to.alert.accept()
  whatsapp("RESULT CAME")
  #results()
 except:
    whatsapp("RESULT CAME")

    
results()
driver.quit()
