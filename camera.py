#from picamera import PiCamera
#from picamera.array import PiRGBArray
import time

from os import path
import sys
from bayBwatch.yoloface_api import _main
from ecapture import ecapture as ec
import time
import cv2
cameraport = 0


class camera:

    def __init__(self):
        """
        initiates a new camera object
        """
        # self.camera = PiCamera()
        self.camera = cv2.VideoCapture(cameraport)


    def is_detecting(self):
        """
        indicates whether a child was detected in danger. Takes a photo, looks
         for a child in it.
        :return: True if a child in danger has been detected, False otherwise.
        """
        self.take_snapshot() # make sure it saves it in the right dir
        if self.detect():
            return True
        return False

    # TODO: Change the third argument's path to the RP dir name + file name
    # TODO: Change all paths to the RP's.
    def detect(self):
        return _main("C:/Users/97252/Desktop/Code/codingprojects/IntegrationBBW/cfg/yolov3-face.cfg",
             "C:/Users/97252/Desktop/Code/codingprojects/IntegrationBBW/model-weights/yolov3-wider_16000.weights",
             "outputs/",
             "image.jpg")

    # TODO: Configure the take_snapshot() method to save the taken snapshot
    #  in the right directory
    def take_snapshot(self):
        return_val, img = self.camera.read()
        cv2.imwrite("image.jpg", img)
        # self.camera.start_preview()
        # time.sleep(5)
        # self.camera.capture('/home/pi/IntegrationBBW/input/image.jpg')
        # self.camera.stop_preview()
        #raw_capture = PiRGBArray(self.camera)
        #time.sleep(0.1)
        #camera.capture(raw_capture, format ="bgr")
        #image = raw_capture.array
        print("taking snap shot")
