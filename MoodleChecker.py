#MoodleChecker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from pyvirtualdisplay import Display

#Main program function
def run(moodleLogin, moodlePassword):
	#Creates browser and logins to personal website
	grades = ''
	display = Display(visible=0, size=(800, 600))
	display.start()
	driver = webdriver.Firefox()
	try:
		driver.get("http://moodle.umn.edu")
		username = driver.find_element_by_name("j_username")
		password = driver.find_element_by_name("j_password")
		username.send_keys(moodleLogin)
		password.send_keys(moodlePassword)
		password.send_keys(Keys.RETURN)
		#Wait for webpage to load
		driver.implicitly_wait(10)
		#Get grade info
		grades = driver.find_element_by_xpath('//*[@id="inst57918"]/div[2]').text
		print("Grades successfully checked at " + str(datetime.now()))
	except Exception as e:
		print(e)
		print("Error getting moodle grades")
	finally:	
		driver.quit()
		display.stop()
	return grades

def runFinal(moodleLogin, moodlePassword):
	#Creates browser and logins to personal website
	finalGrades = ''
	display = Display(visible=0, size=(800, 600))
	display.start()
	driver = webdriver.Firefox()
	try:
		driver.get("https://www.myu.umn.edu/psp/psprd/EMPLOYEE/CAMP/s/WEBLIB_IS_DS.ISCRIPT1.FieldFormula.IScript_DrawSection?group=UM_SSS&section=UM_SSS_GRADES")
		username = driver.find_element_by_name("j_username")
		password = driver.find_element_by_name("j_password")
		username.send_keys(moodleLogin)
		password.send_keys(moodlePassword)
		password.send_keys(Keys.RETURN)
		#Wait for webpage to load
		driver.implicitly_wait(10)
		#Get grade info
		finalGrades = driver.find_element_by_xpath('//*[@id="grades_Undergraduate"]/div[1]/div[3]/div/table').get_attribute('innerHTML')
		print("Final grades successfully checked at " + str(datetime.now()))
	except Exception as e:
		print(e)
		print("Error getting moodle final grades")
	finally:	
		driver.quit()
		display.stop()
	return finalGrades