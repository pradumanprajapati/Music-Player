from pygame import mixer
from tkinter import *
import os
from pygame import *
from tkinter import *
import tkinter.font as font

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing\\n")
    mixer.music.play()


root=Tk()
root.title('Music player')
image_icon = PhotoImage(file=r"D:\Project\Music Player Project-2\proj_img\music icon.png")
root.iconphoto(False,image_icon)

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

def Pause():
    mixer.music.pause()


# to stop the  song
def Stop():
    mixer.music.stop()
    songs.selection_clear(ACTIVE)


# to resume the song

def Resume():
    mixer.music.unpause()


# Function to navigate from the current song
def Previous():
    # to get the selected song index
    previous_one = songs.curselection()
    # to get the previous song index
    previous_one = previous_one[0] - 1
    # to get the previous song
    temp2 = songs.get(previous_one)
    temp2 = (r"D:\Project\Music Player Project-2\New folder")
    mixer.music.load(temp2)
    mixer.music.play()
    songs.selection_clear(0, END)
    # activate new song
    songs.activate(previous_one)
    # set the next song
    songs.selection_set(previous_one)


def Next():
    # to get the selected song index
    next_one = songs.curselection()
    # to get the next song index
    next_one = next_one[0] + 1
    # to get the next song
    temp = songs.get(next_one)
    temp = (r"D:\Project\Music Player Project-2\New folder")
    mixer.music.load(temp)
    mixer.music.play()
    songs.selection_clear(0, END)
    # activate newsong
    songs.activate(next_one)
    # set the next song
    songs.selection_set(next_one)



#playlist---------------

playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)

os.chdir(r'D:\Project\Music Player Project-2\New folder')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

# playbtn=Button(root,text="play",command=playsong)
# playbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
# playbtn.grid(row=1,column=0)

defined_font = font.Font(family='Helvetica')
# Play Button
playbutton = Button(root, text="Play", width=7, command=playsong)
playbutton['font'] = defined_font
playbutton.grid(row=1, column=0)
# pause button
pause_button = Button(root, text="Pause", width=7, command=Pause)
pause_button['font'] = defined_font
pause_button.grid(row=1, column=1)

# stop button
stop_button = Button(root, text="Stop", width=7, command=Stop)
stop_button['font'] = defined_font
stop_button.grid(row=1, column=2)

# resume button
Resume_button = Button(root, text="Resume", width=7, command=Resume)
Resume_button['font'] = defined_font
Resume_button.grid(row=1, column=3)

# previous button
previous_button = Button(root, text="Prev", width=7, command=Previous)
previous_button['font'] = defined_font
previous_button.grid(row=1, column=4)

# nextbutton
next_button = Button(root, text="Next", width=7, command=Next)
next_button['font'] = defined_font
next_button.grid(row=1,column=5)

mainloop()