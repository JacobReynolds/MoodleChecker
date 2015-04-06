#MoodleCheckerTimer
from MoodleChecker import run
import smtplib
import getpass
import time
from datetime import datetime
moodleLogin = input("Please input your x500: ")
moodlePassword = getpass.getpass("Please enter your password: ")
gmailUsername = input("Please input Non-UMN Gmail: ")
gmailPassword = getpass.getpass("Please enter Gmail password: ")

lastIteration = ''
while(True):
	#If the grades have changed since the program started running
	#Send email to user and update to new grades
	#If an error occurs, send email to user and restart
	try: msg = run(moodleLogin, moodlePassword)
	except: 
		print("Error connecting " + str(datetime.now()))
		msg = "Error connecting " + str(datetime.now())
		time.sleep(10)
	if (msg != lastIteration):
		#Sends message using Gmail servers
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(gmailUsername,gmailPassword)
		server.sendmail(gmailUsername,gmailUsername,msg)
		server.quit()
		print("Message sent")
		lastIteration = msg	
	#Wait 60 seconds then restart loop
	time.sleep(60)

