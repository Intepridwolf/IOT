#import time and picamera library
import picamera
from time import sleep

#create object for PiCamera class
camera = picamera.PiCamera()

#set resolution
camera.resolution = (1280, 720)
camera.brightness = 60
camera.start_preview()

#Camera warmup time
sleep(2)

#store image
camera.capture('/home/pi/Pictures/image1.jpeg')
camera.stop_preview()
