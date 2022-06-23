import jetson.inference
import jetson.utils
import smtplib, ssl
import time

sender_email = input("Please type the email you want the email to be sent from... (burner gmail acc) ")
sender_pass = input("Please type the password of the burner account... ")
recip_email = input("Please type the email you would like notifications sent to... ")
subj='Person detected!'
date='6/23/22'
message_text='Alert! there has been someone snooping around, you should check on this...'
server = smtplib.SMTP('smtp.mail.yahoo.com',587)
msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( sender_email, recip_email, subj, date, message_text )
print("email setup complete!\nstarting detectmodel...")

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file

while display.IsStreaming():
	img = camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

	for detection in detections:
		class_name = "reset"
		class_name = net.GetClassDesc(detection.ClassID)
		print(f"Detected '{class_name}'")
		if (class_name == "person"):
			print("Person detected!")
			try:
				print("email setup in progress... ")
				#sever.ehlo()
				#print("server pinged!")
				print("logging in...")
				server.login(sender_email, sender_pass)
				print("Attempting to send email...")
				server.sendmail(sender_email, recip_email, msg)
				print("mail sent!")
				print("logging out of email...")
				server.quit()
				print("logged out!\npasuing script for 10 minutes...")
				time.sleep(600)
			except:
				print("Sorry, somthing went wrong...")
			

