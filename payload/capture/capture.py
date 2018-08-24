import os, sys
from VideoCapture import Device

class Screen:
    def capture(self, file_name):
        if sys.platform == "darwin":
            os.system("screencapture " + file_name + ".png")
        elif sys.platform.system() == "Windows":
            from PIL import ImageGrab
            snapshot = ImageGrab.grab()
            save_path = os.getcwd() + "\\" + file_name + ".jpg"
            snapshot.save(save_path)

class Webcam:
    def capture(self, file_name):    
        from cv2 import *
sdc
        cam = VideoCapture(0) # 0 -> index of camera
        s, img = cam.read()
        if s: # If frame is captured without any errors
            namedWindow("wcam", CV_WINDOW_AUTOSIZE)
            imshow("wcam", img)
            waitKey(0)
            destroyWindow("wcam")
            imwrite(file_name + ".jpg", img) # save image

def screen():
    scr = Screen()
    scr.capture("test")
def cam():
    webc = Webcam()
    webc.capture("test")

# screen()
cam()