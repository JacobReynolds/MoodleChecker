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

#Sends message using Gmail servers
def sendEmail(msg):
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(gmailUsername,gmailPassword)
	server.sendmail(gmailUsername,gmailUsername,msg)
	server.quit()
	
while(True):
	#If the grades have changed since the program started running
	#Send email to user and update to new grades
	#If an error occurs, send email to user and restart
	try: msg = run(moodleLogin, moodlePassword)
	except Exception as e: 
		print("Error connecting " + str(datetime.now()))
		msg = "Error connecting " + str(datetime.now())
		time.sleep(10)
	finally:
		date = datetime.now()
		#Send a health check at 8 am every morning
		if (date.hour == 8 and date.minute <= 1):
			sendEmail("Server healthy")
			print("health check sent")
	if (msg != lastIteration):
		sendEmail(msg)
		print("Message sent")
		lastIteration = msg	
	#Wait 60 seconds then restart loop
	time.sleep(60)