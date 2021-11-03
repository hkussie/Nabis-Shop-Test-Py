import time
import unittest 
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestAgeRestrictionRedirectionModal(unittest.TestCase): 

	# Setup browser
	def setUp(self):
		self.driver = webdriver.Chrome()

	# Navigate to the age restriction modal, hit enter button and then scroll down to the bottom of the page
	def test_age_modal_enter_button(self):
		driver = self.driver 
		driver.get("http://shop.nabis.com/")
		time.sleep(10)
		driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/span/button').click()
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		
	# Close the browser
	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()