#AstronomyChecker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from pyvirtualdisplay import Display

#Main program function
def runAst():
	#Creates browser and logins to personal website
	display = Display(visible=0, size=(800, 600))
	display.start()
	driver = webdriver.Firefox()
	driver.get("http://www.astro.umn.edu/courses/1001/AST_grades.html")
	#Wait for webpage to load
	driver.implicitly_wait(10)
	grades = driver.page_source
	print("Astronomy successfully checked at " + str(datetime.now()))
	driver.quit()
	display.stop()
	return grades
