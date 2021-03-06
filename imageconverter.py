import cv2
import os
import moviepy.editor as mp

vidcap = cv2.VideoCapture('Top Gun.mp4')
directory = r'C:/Users/ianva/Documents/GitHub/mdm2-rep4/images/'
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        os.chdir(directory)
        cv2.imwrite("image "+str(count)+".jpg", image)
    return hasFrames

sec = 0
frameRate = 0.1
count=1
success = getFrame(sec)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
    