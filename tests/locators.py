import random
from selenium.webdriver.common.by import By

"""
1.service frame
2.exceptions
3.range query
4.assertions
"""
#1
TEXT_FORM = (By.XPATH, "//div[@id='app']/div/div/div/div/div/div/div[3]/div/div/div/div/input")
#TEXT_FORM = (By.XPATH, "//input[@value='']")


#Random number method added to Text Form locator in the case that the first feature listed is NOT a form
TEXT_FORM_VAR = "//div[@id='app']/div/div/div/div/div/div/div[3]/div/div[{n}]/div/div/input"
PREDICTION = (By.XPATH,"//div[@id='app']/div/div/div/div/div/div[2]/div/div/div/button/span/h6")
#PREDICTION = (By.CSS_SELECTOR,".jss75")

#2
NO_SERVICE = (By.XPATH,"//p[contains(.,'This project has no AI Service.')]")
SUSPENDED_SERVICE = (By.XPATH,"//p[contains(.,'The owner of the project has suspended the AI service.')]")

#3
RQ_SWITCH  = (By.XPATH, "//div[@id='app']/div/div/div/div/div/div/div[2]/div/div[2]/div/span/span/span/input")
RQ_FEATURE = (By.XPATH, "//div[@id='app']/div/div/div/div/div/div/div[3]/div/div/div/span/div/span/span/input")
RQ_FEATURE_VAR = "//div[@id='app']/div/div/div/div/div/div/div[3]/div[{n}]/div/div/span/div/span/span/input"


RQ_START = (By.XPATH, "//div[@id='app']/div/div/div/div/div/div/div[3]/div[3]/div/div/div/div/input")
#Locator declared in test function, using string var below
RQ_START_VAR = "//div[@id='app']/div/div/div/div/div/div/div[3]/div[3]/div[{n}]/div/div/div/input"

INSIGHT_BUTTON = (By.CSS_SELECTOR, ".MuiIconButton-colorPrimary .MuiSvgIcon-root")


#4

VALID_TEXT = (By.XPATH, "//h5[contains(.,'Prediction: ')]")
INVALID_TEXT = (By.XPATH, "//span[contains(.,'Unable to make prediction.')]")
BLANK = (By.XPATH, "//h6[contains(.,'Please enter a value for ')]")
INSIGHT_POINTER = (By.XPATH, "//h6[contains(.,'Model: ')]")
INSIGHT_CHART = (By.XPATH, "//h2[contains(.,'Model Coefficients')]")
INSIGHT_CHART_KNN = (By.XPATH, "//h2[contains(.,'KNN Distance')]")



