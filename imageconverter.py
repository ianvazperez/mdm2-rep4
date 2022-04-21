import cv2
import os

vidcap = cv2.VideoCapture('video.mp4')
directory = r'C:/Users/ianva/OneDrive/mdm2-rep4/images/'
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        os.chdir(directory)
        cv2.imwrite("image "+str(count)+".jpg", image)
    return hasFrames

sec = 0

frameRate = 0.5

count=1

success = getFrame(sec)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
    