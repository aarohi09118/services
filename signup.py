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

driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//button[@class='text-sm lg:text-xs bg-theme-blue w-5 h-5 px-1 rounded-full text-white btn-cookie fixed bottom-8 -right-1 md:bottom-4 mr-2 md:mr-0']").click()
driver.find_element(By.XPATH,"//span[text()='Login / SignUp']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter Email']").send_keys("gctfgvygb.university@yopmail.com")
driver.find_element(By.XPATH,"//div[text()='Login']").click()
driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys("Mannu")
driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys("testing")
driver.find_element(By.ID,"contactNumber").send_keys("9012659233")
driver.find_element(By.XPATH,"//div[text()='Sign Up']").click()
driver.find_element(By.XPATH,"//input[@name='otp0']").send_keys("1")
driver.find_element(By.XPATH,"//input[@name='otp1']").send_keys("2")
driver.find_element(By.XPATH,"//input[@name='otp2']").send_keys("3")
driver.find_element(By.XPATH,"//input[@name='otp3']").send_keys("4")
driver.find_element(By.XPATH,"//input[@name='otp4']").send_keys("5")
time.sleep(5)

