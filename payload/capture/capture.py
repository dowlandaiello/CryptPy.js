import os, sys

class ScreenCapture:
    def capture(self, file_name):
        if sys.platform == "darwin":
            os.system("screencapture " + file_name + ".png")
        elif sys.platform.system() == "Windows":
            from PIL import ImageGrab
            snapshot = ImageGrab.grab()
            save_path = "C:\\Users\\YourUser\\Desktop\\MySnapshot.jpg"
            snapshot.save(save_path)

sc = ScreenCapture()
sc.capture("asd")