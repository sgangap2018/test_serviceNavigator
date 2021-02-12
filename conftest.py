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

#Project page URL
URL_SERVICE = 'https://aiclub.world/projects/{s}?tab=service'


IDS = ['41bf4dca-6c27-4f95-adac-3be6f34ea422','cae0bf61-2ad2-4ad5-b644-9e25cb0c076d']

@pytest.fixture(scope='class', params=IDS)
def session_feeder(request):
	driver = webdriver.Remote(
            command_executor='http://172.17.0.1:4444',
			desired_capabilities = {
			'browserName': 'chrome',
			'javascriptEnabled': True
		}
	)
	driver.get(URL_SERVICE.format(s=request.param))
	request.cls.driver = driver
	yield
	driver.quit()