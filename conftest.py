import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import json
import test_args



#Project page URL
URL_SERVICE = 'https://aiclub.world/projects/{s}?tab=service'

#get project ID args
IDS = test_args.get_args()


@pytest.fixture(scope='class', params=IDS)
def session_feeder(request):
	#set up headless browser
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--window-size=1440, 900")
	capabilities = chrome_options.to_capabilities()
	driver = webdriver.Chrome(desired_capabilities=capabilities)

	driver.get(URL_SERVICE.format(s=request.param))
	request.cls.driver = driver
	yield
	driver.quit()