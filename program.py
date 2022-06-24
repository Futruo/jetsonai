import jetson.inference
import jetson.utils
import smtplib, ssl
import time
# Defining veriables
sender_email = input("Please type the email you want the email to be sent from... (burner gmail acc) ")
sender_pass = input("Please type the password of the burner account... ")
recip_email = input("Please type the email you would like notifications sent to... ")
subj='Person detected!'
date='6/23/22'
message_text='Alert! there has been someone snooping around, you should check on this...'
server = smtplib.SMTP('smtp.mail.yahoo.com',587) # Establishing server veriable
msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( sender_email, recip_email, subj, date, message_text )
print("email setup complete!\nstarting detectmodel...")

# Start detectnet model
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0") # 'csi://0' for MIPI CSI camera
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file
print("System ready!\nPausig for 3 minutes to prevent faulse alarms...")
time.sleep(180)

# Show live cam feed
while display.IsStreaming():
	img = camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

	for detection in detections:
		class_name = "reset" # Resets veriable to prevent false alarms
		class_name = net.GetClassDesc(detection.ClassID)
		print(f"Detected '{class_name}'")
		if (class_name == "person"):
			print("Person detected!")
			try:
				print("email setup in progress... ")
				print("logging in...")
				server.login(sender_email, sender_pass) # connects to server
				print("Attempting to send email...")
				server.sendmail(sender_email, recip_email, msg) # actually sending notification
				print("mail sent!")
				print("logging out of email...")
				server.quit() # logs out
				print("logged out!\npasuing script for 10 minutes...")
				time.sleep(600)
			except:
				print("Sorry, somthing went wrong...") #fallback message
			

