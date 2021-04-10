#from picamera import PiCamera
#from picamera.array import PiRGBArray
import time
# from bayBwatch.yoloface_api import _main


class camera:

    def __init__(self):
        """
        initiates a new camera object
        """

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

    # TODO: Change the third argument's path to the right dir name + file name
    def detect(self):
        return True
        # _main("C:/Users/97252/Desktop/Code/codingprojects/BayBWatchIntegration/bayBwatch/cfg/yolov3-tiny.cfg",
        #       "C:/Users/97252/Desktop/Code/codingprojects/BayBWatchIntegration/bayBwatch/model-weights/yolov3-tiny.weights",
        #       "outputs/",
        #       "C:/Users/97252/Desktop/Code/codingprojects/BayBWatchIntegration/bayBwatch/assets/blackfamily.jpg")

    # TODO: Configure the take_snapshot() method to save the taken snapshot
    #  in the right directory
    def take_snapshot(self):
        #camera = PiCamera()
        #raw_capture = PiRGBArray(camera)
        #time.sleep(0.1)
        #camera.capture(raw_capture, format ="bgr")
        #image = raw_capture.array
        print("taking snap shot")
