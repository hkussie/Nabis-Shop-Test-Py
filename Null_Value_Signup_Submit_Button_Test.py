import time 
import unittest 
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class NullValueSignupSubmitButtonTest(unittest.TestCase):
	# Setup browser
	def setUp(self):
		self.driver = webdriver.Chrome()

	# Navigate to the age restriction modal, hit enter button and then scroll down to the bottom of the page
	def test_null_value_response(self):
		driver = self.driver 
		driver.get("http://shop.nabis.com/")
		time.sleep(5)
		driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/span/button').click()
		driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/form/div[4]/button').click()
		self.first_required_field_message = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/form/div[1]/label/div')
		self.second_required_field_message = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/form/div[2]/div/label/div')
		self.third_required_field_message = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/form/div[3]/div/label/div')
		self.expectedRequiredFieldMessage = "Required"
		self.assertEqual(self.first_required_field_message.text, self.expectedRequiredFieldMessage)
		self.assertEqual(self.second_required_field_message.text, self.expectedRequiredFieldMessage)
		self.assertEqual(self.third_required_field_message.text, self.expectedRequiredFieldMessage)

	# Close the browser
	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()