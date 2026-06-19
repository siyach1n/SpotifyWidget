import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap

app = QApplication(sys.argv)

#oject holds the window of widget
window = QWidget() 


#Remember where the mouse is clicked 
def mousePressEvent(event):
    window.old_pos = event.globalPosition().toPoint()

def mouseMoveEvent(event):
    new_pos = event.globalPosition().toPoint() #Get current mouse position.
    delta = new_pos - window.old_pos # calulate How far did the mouse move
    #Remember where the mouse is
    window.move(
    window.x() + delta.x(),
    window.y() + delta.y()
    )
    window.old_pos = new_pos



window.mousePressEvent = mousePressEvent
window.mouseMoveEvent = mouseMoveEvent

window.old_pos = QPoint(200,80)

#to show the song title inside the window 
song_title = QLabel("Once Upon a Dream",window) 

#to show the artist name  inside the window 
artist = QLabel("Lana Del Rey",window)  

album_art = QLabel(window)

album_art.move(10,10)

album_art.resize(60,60)

pixmap = QPixmap("album.jpg")

pixmap = pixmap.scaled(60,60)

album_art.setPixmap(pixmap) 



 #move the title in the window with padding
song_title.move(150,15)

#move the artist name in the window with padding
artist.move(150,40) 


 #to resizing the window sized
window.resize(350, 80)



#color inside the window
window.setStyleSheet("""
    background-color: green;
    border-radius: 40px;
""")

#the title of the window
window.setWindowTitle("My Spotify Widget")

#to remove the winodw title and the drag and close button to clean ui
window.setWindowFlags(
    Qt.FramelessWindowHint
)

#to display the ui of the windowE
window.show()

app.exec()