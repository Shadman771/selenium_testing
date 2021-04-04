import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

# Use Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("http://automationpractice.com/index.php")
driver.find_element_by_xpath("/html/body/div/div[1]/header/div[2]/div/div/nav/div[1]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id=\"email_create\"]").send_keys("sa.m.ple@gmail.com")
driver.find_element_by_xpath("//*[@id=\"SubmitCreate\"]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='customer_firstname']").send_keys("Abdullah Al")
driver.find_element_by_xpath("//*[@id='customer_lastname']").send_keys("Faroque")
driver.find_element_by_xpath("//*[@id='passwd']").send_keys("123456")


# CheckBox
driver.find_element_by_xpath("//*[@id='newsletter']").click()



driver.find_element_by_xpath("//*[@id='address1']").send_keys("Maniknagar, Dhaka")
driver.find_element_by_xpath("//*[@id='city']").send_keys("Dhaka")

state = Select(driver.find_element_by_name("id_state"))
state.select_by_visible_text("Arizona")

driver.find_element_by_xpath("//*[@id='postcode']").send_keys("00000")
driver.find_element_by_xpath("//*[@id='phone_mobile']").send_keys("01521259370")
driver.find_element_by_xpath("//*[@id='alias']").send_keys("Dhaka")
driver.find_element_by_xpath("//*[@id='submitAccount']").click()
# I'm stuck here
days = Select(driver.find_element_by_name("days"))
days.select_by_visible_text("10")

months = Select(driver.find_element_by_name("months"))
months.select_by_visible_text("August")

years = Select(driver.find_element_by_name("years"))
years.select_by_visible_text("1985")