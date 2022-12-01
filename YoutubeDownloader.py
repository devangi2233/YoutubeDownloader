from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from pytube import YouTube
from moviepy import *
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip

#function
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_mp4_file():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

def download_mp3_file():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    mp3_video = YouTube(get_link).streams.get_audio_only().download()
    aud_clip = AudioFileClip(mp3_video)
    aud_clip.close()
    
    
screen = Tk()
title = screen.title("Yotube Downloader")
canvas = Canvas(screen, width=600, height=600)
canvas.pack()

# image logo
img= (Image.open("image.png"))

# resize image
resized_image= img.resize((300,120), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

canvas.create_image(300,100, image=new_image)

#Link filed
link_field = Entry(screen, width=35, background="firebrick2", foreground="white", font=("Comic Sans MS", 14))
link_label = Label(screen, text = "Enter Download Link : ", font=("Comic Sans MS", 18))
canvas.create_window(300,210, window=link_label)
canvas.create_window(300,250, window=link_field)

#select path for saving file
path_label = Label(screen, text="select path for download", font=("Comic Sans MS", 18))
select_btn = Button(screen, text="select", width=6, height=1,background="firebrick2", foreground="white", font=("Comic Sans MS", 14), command=select_path)

canvas.create_window(300, 320, window=path_label)
canvas.create_window(300, 380, window=select_btn)

#download btn
download_mp4_btn = Button(screen, text="Download Mp4", width=13, height=1,background="firebrick2", foreground="white", font=("Comic Sans MS", 14), command=download_mp4_file)
canvas.create_window(200, 460, window=download_mp4_btn)

download_mp3_btn = Button(screen, text="Download Mp3", width=13, height=1,background="firebrick2", foreground="white", font=("Comic Sans MS", 14), command=download_mp3_file)
canvas.create_window(380, 460, window=download_mp3_btn)


screen.mainloop()
