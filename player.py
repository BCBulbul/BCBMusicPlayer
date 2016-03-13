import musicplayer
from tkinter import *

#development

player = musicplayer.createPlayer()
player.outSamplerate = 96000 # support high quality :)
player.queue = songs()
player.peekQueue = peekSongs


window = Tkinter.Tk()
window.title("BCB Music Player")
songLabel = Tkinter.StringVar()

def onSongChange(**kwargs): songLabel.set(pprint.pformat(player.curSongMetadata))
def cmdPlayPause(*args): player.playing = not player.playing
def cmdNext(*args): player.nextSong()

Tkinter.Label(window, textvariable=songLabel).pack()
Tkinter.Button(window, text="Play/Pause", command=cmdPlayPause).pack()
Tkinter.Button(window, text="Next", command=cmdNext).pack()

player.onSongChange = onSongChange
player.playing = True # start playing
window.mainloop()