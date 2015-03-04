#MoodleChecker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime

#Main program function
def run(moodleLogin, moodlePassword):
	#Creates browser and logins to personal website
	driver = webdriver.Firefox()
	driver.get("http://moodle.umn.edu")
	username = driver.find_element_by_name("j_username")
	password = driver.find_element_by_name("j_password")
	username.send_keys(moodleLogin)
	password.send_keys(moodlePassword)
	password.send_keys(Keys.RETURN)
	#Wait for webpage to load
	driver.implicitly_wait(10)
	info = driver.find_element_by_xpath('//*[@id="inst39"]/div[2]')
	#Get grade info
	html = info.get_attribute('innerHTML')

	grades = driver.find_element_by_xpath('//*[@id="inst39"]/div[2]').text

	print("Grades successfully checked at " + str(datetime.now()))
        driver.quit()
	return grades
