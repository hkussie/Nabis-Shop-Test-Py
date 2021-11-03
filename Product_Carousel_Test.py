import time
import unittest 
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestProductCarousel(unittest.TestCase): 

	# Setup browser
	def setUp(self):
		self.driver = webdriver.Chrome()

	# Navigate product carousel to the right, ensure that the text values from product list don't match product description
	def test_product_carousel_functionality_right_click(self):
		driver = self.driver 
		driver.get("http://shop.nabis.com/")
		time.sleep(10)
		driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/span/button').click()
		self.first_product_description = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[1]/div/div/div[4]/div/div/div[2]/div[1]/div/div/h1')
		self.second_product_description = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[1]/div/div/div[5]/div/div/div[2]/div[1]/div/div/h1')
		self.third_product_description = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[1]/div/div/div[6]/div/div/div[2]/div[1]/div/div/h1')
		driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[2]/div[2]').click()
		self.first_right_click_product_description = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[1]/div/div/div[7]/div/div/div[2]/div[1]/div/div/h1')
		self.second_right_click_product_description = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/div/div/h1')
		self.third_right_click_product_description = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[1]/div/div/div[9]/div/div/div[2]/div[1]/div/div/h1')
		self.assertNotEqual(self.first_product_description.text, self.first_right_click_product_description.text)
		self.assertNotEqual(self.second_product_description.text, self.second_right_click_product_description.text)
		self.assertNotEqual(self.third_product_description.text, self.third_right_click_product_description.text)

	# Navigate product carousel to the left, ensure that text values from product list don't match product description 
	def test_product_carousel_functionality_left_click(self): 
		driver = self.driver 
		driver.get("http://shop.nabis.com/")
		time.sleep(10)
		driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/span/button').click()
		self.first_product_description = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[1]/div/div/div[4]/div/div/div[2]/div[1]/div/div/h1')
		self.second_product_description = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[1]/div/div/div[5]/div/div/div[2]/div[1]/div/div/h1')
		self.third_product_description = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[1]/div/div/div[6]/div/div/div[2]/div[1]/div/div/h1')
		time.sleep(5)
		driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[2]/div[1]').click()
		time.sleep(5)
		self.first_left_click_product_description = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[1]/div/div/div[16]/div/div/div[2]/div[1]/div/div/h1')
		self.second_left_click_product_description = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[1]/div/div/div[17]/div/div/div[2]/div[1]/div/div/h1')
		self.third_left_click_product_description = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/section[1]/div[1]/div/div/div[18]/div/div/div[2]/div[1]/div/div/h1')
		time.sleep(5)
		self.assertNotEqual(self.first_product_description.text, self.first_left_click_product_description.text)
		self.assertNotEqual(self.second_product_description.text, self.second_left_click_product_description.text)
		self.assertNotEqual(self.third_product_description.text, self.third_left_click_product_description.text)

	# Validate each product section for nabis product page 
	def test_validate_each_product_section_in_shop_nabis(self):
		driver = self.driver
		driver.get("http://shop.nabis.com/")
		time.sleep(10)
		driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/span/button').click()
		self.newest_drop_section_title = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]')
		self.recommended_for_you_section_title = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/h1')
		self.popular_near_you_section_title = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div/div[1]/h1')
		self.most_affordable_section_title = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[4]/div/div[1]/h1')
		self.nabis_potluck_section_title = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[5]/div/div[1]/h1')
		self.flower_section_title = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[7]/div/div[1]/h1')
		self.edibles_section_title = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[6]/div/div[1]/h1')
		self.pre_rolls_section_title = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[8]/div/div[1]/h1')
		self.based_on_on_your_purchases_title_section = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[9]/div/div[1]/h1')
		self.popular_near_you_region_section_title = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[10]/div/div[1]/h1')
		# Expected values for assertionStatements 
		self.expected_newest_drop_section_title = 'Newest Drops'
		self.expected_recommended_for_you_section_title = 'Recommended For You'
		self.expected_popular_near_you_section_title = 'Popular Near You'
		self.expected_most_affordable_section_title = 'Most Affordable'
		self.expected_nabis_potluck_section_title = 'Nabis Potluck'
		self.expected_edibles_section_title = 'Edibles'
		self.expected_flower_section_title = 'Flower'
		self.expected_pre_rolls_section_title = 'Pre-Rolls'
		self.expected_based_on_your_purchases_title_section = 'Based on Your Purchases'
		self.expected_popular_near_you_region_section_title = 'Popular Near You'
		# Assert Statements
		self.assertEqual(self.newest_drop_section_title.text, self.expected_newest_drop_section_title)
		self.assertEqual(self.recommended_for_you_section_title.text, self.expected_recommended_for_you_section_title)
		self.assertEqual(self.expected_popular_near_you_section_title, self.popular_near_you_section_title.text)
		self.assertEqual(self.most_affordable_section_title.text, self.expected_most_affordable_section_title)
		self.assertEqual(self.nabis_potluck_section_title.text, self.expected_nabis_potluck_section_title)
		self.assertEqual(self.flower_section_title.text, self.expected_flower_section_title)
		self.assertEqual(self.pre_rolls_section_title.text, self.expected_pre_rolls_section_title)
		self.assertEqual(self.based_on_on_your_purchases_title_section.text, self.expected_based_on_your_purchases_title_section)
		self.assertEqual(self.popular_near_you_region_section_title.text, self.expected_popular_near_you_region_section_title)
		self.assertEqual(self.edibles_section_title.text, self.expected_edibles_section_title)

	# Close the browser
	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()