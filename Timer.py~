#MoodleCheckerTimer
from MoodleChecker import run
import smtplib
import getpass
import time
moodleLogin = raw_input("Please input your x500: ")
moodlePassword = getpass.getpass("Please enter your password: ")
gmailUsername = raw_input("Please input Non-UMN Gmail: ")
gmailPassword = getpass.getpass("Please enter Gmail password: ")

lastIteration = ''
while(True):
	msg = run(moodleLogin, moodlePassword)
	if (msg != lastIteration):
		#Sends message using Gmail servers
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(gmailUsername,gmailPassword)
		server.sendmail(gmailUsername,gmailUsername,msg)
		server.quit()
		print("Message sent")
		lastIteration = msg
		time.sleep(60)

