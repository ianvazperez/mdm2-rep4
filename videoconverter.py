from moviepy.editor import *
import os

directory = r'C:/Users/ianva/Documents/GitHub/mdm2-rep4/images/'
clips = []
img_number=1

for img_number in range(1,1505): 
    clip =  ImageClip(directory + 'cropped ' + str(img_number) + '.jpg').set_duration(0.1)
    clips.append(clip)


video_clip = concatenate_videoclips(clips, method='compose')
video_clip.write_videofile("cropped-video(1504).mp4", fps=24, remove_temp=True, codec="libx264", audio_codec="aac")

os.chdir(r'C:/Users/ianva/Documents/GitHub/mdm2-rep4/')
original_video = VideoFileClip(r"video.mp4")
original_video.audio.write_audiofile(r"audio.mp3")

audio_clip = AudioFileClip("audio.mp3")
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile("cropped-video-final(1504).mp4", fps=24, remove_temp=True, codec="libx264", audio_codec="aac")