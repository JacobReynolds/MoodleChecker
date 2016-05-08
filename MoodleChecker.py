#MoodleChecker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from pyvirtualdisplay import Display

#Main program function
def run(moodleLogin, moodlePassword):
	print("start moodle")
	#Creates browser and logins to personal website
	display = Display(visible=0, size=(800, 600))
	display.start()
	driver = webdriver.Firefox()
	driver.get("http://moodle.umn.edu")
	username = driver.find_element_by_name("j_username")
	password = driver.find_element_by_name("j_password")
	username.send_keys(moodleLogin)
	password.send_keys(moodlePassword)
	password.send_keys(Keys.RETURN)
	#Wait for webpage to load
	driver.implicitly_wait(10)
	info = driver.find_element_by_xpath('//*[@id="inst57918"]/div[2]')
	#Get grade info
	html = info.get_attribute('innerHTML')

	grades = driver.find_element_by_xpath('//*[@id="inst57918"]/div[2]').text

	print("Grades successfully checked at " + str(datetime.now()))
	driver.quit()
	display.stop()
	print("finish moodle")
	return grades
