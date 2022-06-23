# jetsonai
Jetson AI Detect Project

Welcome!

This project is a proof of concept for a system desnined to send emails when a person is detected! 
Google recently made it so 3rd party apps no longer can access gmail through insecure methods such as no ssl encryption. This complicates things greatly and most services are the same way.

Thanks for looking at this project! I hope it exceeds your expecations
-Garison

# Prerequisites

1. Jetson nano
2. USB webcam
3. HDMI cable, keyboard, mouse (optional)

# How to run

The steps for runnings this program are simple!

Install and clone "jetson-inference"

sudo apt-get update
sudo apt-get install git cmake

git clone --recursive https://github.com/dusty-nv/jetson-inference
cd jetson-inference
git submodule update --init


sudo apt-get install libpython3-dev python3-numpy

mkdir build
cd build
cmake ../

sudo make install
sudo ldconfigRun
