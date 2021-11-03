import time 
import unittest 
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestAgeRestrictionRedirectionModal(unittest.TestCase): 

	# Create browser instance
	def setUp(self):
		self.driver = webdriver.Chrome()

	# Main test method
	def test_age_modal_redirection(self):
		driver = self.driver 
		driver.get("http://shop.nabis.com/")
		time.sleep(10)
		driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/a/span/button').click()
		self.redirectURL = driver.current_url
		self.expectedURL = "https://www.nabis.com/"
		self.assertEqual(self.redirectURL, self.expectedURL)

	# Close the browser
	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()