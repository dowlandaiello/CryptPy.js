import os, sys

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
        if sys.platform == "darwin":
            os.system("screencapture " + file_name + ".png")
        elif sys.platform.system() == "Windows":
            from PIL import ImageGrab
            snapshot = ImageGrab.grab()
            save_path = "C:\\Users\\YourUser\\Desktop\\MySnapshot.jpg"
            snapshot.save(save_path)

def screen():
    scr = Screen()
    scr.capture("test")
def cam():
    webc = Webcam()
    webc.capture("test")

# screen()
cam()