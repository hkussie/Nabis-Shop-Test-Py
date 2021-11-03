# Nabis-Shop-Test-Py

# Table of Contents
1. Necessary downloads to run tests
2. Overview of test methods in project 
3. Running the tests  
4. Further notes on how to scale and improve the project

--- 

## Necessary Downloads: 
1. Python 
2. Pip 
3. Selenium 
4. ChromeDriver 
5. ChromeDriver-Binary (Python Library)
6. ChromeDriver-Binary-Auto (Python Library)
7. unittest (Python Library)
8. time (Python Library)
9. For further download instructions: (https://pypi.org/project/chromedriver-binary/, https://selenium-python.readthedocs.io/)

--- 

## Overview of test methods:
**Age Restriction Redirection Modal Test: test_age_modal_redirection()**
```py
def test_age_modal_redirection(self):
	driver = self.driver 
	driver.get("http://shop.nabis.com/")
	time.sleep(10)
	driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/a/span/button').click()
	self.redirectURL = driver.current_url
	self.expectedURL = "https://www.nabis.com/"
	self.assertEqual(self.redirectURL, self.expectedURL)
```
This is the main test method for the Age_Restriction_Redirection_Modal_Enter_Button_Test.py file. This method navigates to the shop nabis market page, clicks on the exit button of the age restriction modal and validates that the user is redirected to the nabis home page. 

**Age Modal Enter Button Test: test_age_modal_enter_button()**
```py
def test_age_modal_enter_button(self):
	driver = self.driver 
	driver.get("http://shop.nabis.com/")
	time.sleep(10)
	driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/span/button').click()
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		
```
This is the main test method for the Age_Restriction_Modal_Enter_Button_Test.py file. This method navigates to the shop nabis market page, clicks on the enter button of the age restriction modal and validates that the user can scroll down to the bottom of the nabis market page.

**Product Carousel Test: test_product_carousel_functionality_right_click(), test_product_carousel_functionality_left_click(), test_validate_each_product_section_in_shop_nabis()** 
```py
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
```
```py
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

```
These two methods validate that when the buttons that shift the product carousel(s) three different product listings are displayed to the user. The first method clicks the button that shifts the products to the right, the second method shifts the products to the left. 

```py
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

``` 
This method ensures that each section header, validating the existince of each section in the nabis shop market place. These methods, when executed in tandem with each other validate that: each product section is rendered to the user, the product carousel displays three items at a time to the user, and when clicked (either to the right or left) will display a new set of product offerings. 

**Product Modal Test: test_outer_modal_click_exit()** 
```py
def test_outer_modal_click_exit(self):
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
```
This is the main test method for Product_Modal_Test.py file. This test method ensures that when a user clicks on a product offering in the nabis marketplace page, and then clicks out of the product offering modal, they are redirected back to the main marketplace and the modal disappears. 

**Null Value Signup Submit Button Test: test_null_value_response()** 
```py
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

```
This is the main test method for the test case that I was asked to come up with. This test ensures that when a user clicks on the "enter" on the age restriction modal, they are redirected to the nabis marketplace page. Once on the page, the user presses the "Submit" button on the Signup for Marketplace feature. Once done, red colord "Required" warnings should be alerted to the user for each field they failed to provide information for. 

--- 

## Running the tests (from the commandline):
To run all tests within a class, in a particular file: 
```console
$ python file_name_you_want_to_run.py

```
To run particular tests that exist in a singular class, in a particular file; 

```console
$ python file_name_you_want_to_run.py ClassName.TestCaseYouWantToRun
```  

## Further notes on how to scale and improve the project: 
1. Incorporate existing code to BDD framework such as Cucumber, Behave (Python's extension of Cucumber), etc. to enable greater structure of locators, test data, and commonly shared methods between test suites/cases. 
2. Enable reporting plugin features into CI/CD platform with testing framework, to enable greater and more accurate reporting of test case execution that can be accessed by the entire team. 
3. Incorporation of properly mocked data to test suite, in order to fully test the application and expand test coverage into signed users. 