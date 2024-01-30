from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = "/Users/apple/Desktop/cd"

opt = Options()
# driver = webdriver.Chrome(service=s, options=opt)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(opt)
driver.implicitly_wait(10)
driver.get("https://universityliving.com")
driver.maximize_window()
checkUrl = "https://www.universityliving.com/services/ga"

driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[@class='text-sm lg:text-xs bg-theme-blue w-5 h-5 px-1 rounded-full text-white btn-cookie fixed bottom-8 -right-1 md:bottom-4 mr-2 md:mr-0']").click()
driver.find_element(By.XPATH,"//a[text()='Services']").click()
driver.find_element(By.XPATH,"//div[text()='Explore All Services']").click()
time.sleep(5)
driver.find_element(By.XPATH,"(//p[text()='Verified guarantors for the ultimate safety net'])[2]").click()

driver.find_element(By.ID,"country").click()
driver.find_element(By.XPATH,"//option[text()='Ireland']").click()
driver.find_element(By.XPATH,"//div[text()='Find A Guarantor']").click()


pageurl = driver.current_url
print(pageurl)
if checkUrl == pageurl:
    print("url is correct")
else:
    print("url is not matching plz check")

print(pageurl)


driver.find_element(By.ID,"email").send_keys("pravin.garg@universityliving.com")
driver.find_element(By.XPATH,"//div[text()='Login']").click()

driver.find_element(By.NAME, "otp0").send_keys("1")
driver.find_element(By.NAME, "otp1").send_keys("2")
driver.find_element(By.NAME, "otp2").send_keys("3")
driver.find_element(By.NAME, "otp3").send_keys("4")
driver.find_element(By.NAME, "otp4").send_keys("5")
driver.find_element(By.CSS_SELECTOR, "form button div").click()
driver.find_element(By.XPATH,"//div[text()='Find A Guarantor']").click()
driver.find_element(By.XPATH,"//div[text()='Submit']").click()

time.sleep(5)
driver.back()

time.sleep(10)
