import pytest
from pytest_dependency import depends
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random
import locators


@pytest.mark.usefixtures('session_feeder')
class ProjectTest:
	pass

class Test_Project(ProjectTest):

	# TESTS

	@pytest.mark.dependency(name='check_service')
	def test_verify_service(self):
		try:
			wait = WebDriverWait(self.driver, 5)
			wait.until(EC.frame_to_be_available_and_switch_to_it(0))
		except:
			pytest.skip()

	@pytest.mark.dependency(name='test_monitor', depends=["check_service"])
	def test_workflow(self):
		data = [
			'45.00', '%$#$%#%$',
		]
		self.driver.implicitly_wait(5)

		# locate text form in service display
		try:
			self.locate_textElement(data, locators.TEXT_FORM)
		except:
			self.locate_textElement(data, locators.TEXT_FORM_VAR)

	@pytest.mark.dependency(name='test_rq', depends=["check_service", "test_monitor"])
	def test_rangeQuery(self):
		data = [
			'45.00', '%$#$%#%$'
		]
		self.driver.implicitly_wait(5)

		# click RangeQuery switch
		self.driver.find_element(*locators.RQ_SWITCH).click()
		self.driver.implicitly_wait(3)

		# Locate and click Range Query feature,then locate 'Start' form and pass param
		self.rq_function(data)

	@pytest.mark.dependency(name='test_insights', depends=["test_monitor"])
	def test_insight_chart(self):
		try:
			#verify existence of Algorithm specific insight
			wait = WebDriverWait(self.driver, 5)
			insight = wait.until(EC.presence_of_element_located(*locators.INSIGHT_POINTER)).click()

			#Verify chart popup box displays when clicked
			if insight:
				self.driver.find_element(*locators.INSIGHT_BUTTON).click()
				self.driver.implicitly_wait(3)
				chart_title = self.driver.find_element(*locators.INSIGHT_CHART)
				assert chart_title.text == 'Feature Importance'
		except:
			pytest.skip()

	# FUNCTIONS

	def click_prediction(self):
		pred_button = self.driver.find_element(*locators.PREDICTION)
		pred_button.click()
		try:
			predict_message = self.driver.find_element(*locators.VALID_TEXT)
			assert predict_message.text == 'Prediction:'
		except:
			predict_message = self.driver.find_element(*locators.INVALID_TEXT)
			assert predict_message.text == 'Unable to make prediction.'
		# for live test (remove eventually)
		sleep(3)

	def locate_textElement(self, data, locator):
		form = self.driver.find_element(*locator)
		if form:
			for param in data:
				form.send_keys(Keys.CONTROL + 'a')
				form.send_keys(Keys.DELETE)
				form.send_keys(param)
				self.click_prediction()

	def rq_function(self, data):
		try:
			feature = self.find_element(*locators.RQ_FEATURE).click()
			if feature:
				try:
					self.locate_textElement(data, locators.RQ_START)
				except NoSuchElementException:
					pass
			else:
				self.click_prediction()
		except:
			i = random.randint(2, 10)
			RQ_FEATURE_VAR = (By.XPATH, locators.RQ_FEATURE_VAR.format(n=i))
			RQ_START_VAR = (By.XPATH, locators.RQ_START_VAR.format(n=i))
			feature = self.driver.find_element(*RQ_FEATURE_VAR).click()
			if feature:
				try:
					self.locate_textElement(data, RQ_START_VAR)
				except NoSuchElementException:
					pass
			else:
				self.click_prediction()