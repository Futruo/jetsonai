# jetsonai
Jetson AI Detect Project

Welcome!

This project is a proof of concept for a system desnined to send emails when a person is detected! 
Google recently made it so 3rd party apps no longer can access gmail through insecure methods such as no ssl encryption. This complicates things greatly and most services are the same way. Thus the email sending function may not work as expected.

Thanks for looking at this project! I hope it exceeds your expecations
-Garison

# Prerequisites

1. Jetson nano
2. python installed
3. USB webcam
4. HDMI cable, keyboard, mouse (optional)


# Limitations

Note that this program will need access to your email account of choice, you must get an app password and or allow less secure apps.

# Additional Notes

This project is open source! Please feel free to take as you wish and edit it as needed. hook up other functions or compleatly rewrite it from the ground up! The choice is yours!

# How to run

The steps for runnings this program are simple!

Install and clone "jetson-inference"

sudo apt-get update,
sudo apt-get install git cmake

git clone --recursive https://github.com/dusty-nv/jetson-inference,
cd jetson-inference,
git submodule update --init


sudo apt-get install libpython3-dev python3-numpy

mkdir build,
cd build,
cmake ../

sudo make install,
sudo ldconfigRun

Download and run "program.py" using
python3 program.py

# Video Demo
https://youtu.be/X12Wrr88GGM
