from moviepy.editor import *
import os

directory = r'C:/Users/ianva/OneDrive/mdm2-rep4/images/'
clips = []
img_number=1

for img_number in range(1,22): 
    clip =  ImageClip(directory + 'image ' + str(img_number) + '.jpg').set_duration(1)
    clips.append(clip)


video_clip = concatenate_videoclips(clips, method='compose')
video_clip.write_videofile("cropped-video.mp4", fps=1, remove_temp=True, codec="libx264", audio_codec="aac")