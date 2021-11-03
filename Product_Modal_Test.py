import time 
import unittest 
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
	
class TestProductModal(unittest.TestCase):
	# Setup browser
	def setUp(self):
		self.driver = webdriver.Chrome()

	# Navigate to the age restriction modal, hit enter button, validate elements in modal, click outside of modal
	def test_age_modal_enter_button(self):
		driver = self.driver 
		driver.get("http://shop.nabis.com/")
		time.sleep(5)
		driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/span/button').click()
		driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[1]/div/div/div[4]/div/div/div[1]/div/span/button').click()
		try: 
			driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div')
			driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[3]/div/div')
		except NoSuchElementException:
			print("Full product description not present")
		driver.find_element_by_xpath('/html/body/div[3]/div/i').click()	

	# Close the browser
	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()