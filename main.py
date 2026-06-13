import sys

from PySide6.QtWidgets import QApplication, QWidget ,QLabel
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget() #oject holds the window of widget

song_title = QLabel("Once Upon a Dream",window) #to show the song title inside the window 

artist = QLabel("Lana Del Rey",window)  #to show the artist name  inside the window 

song_title.move(100,15) #move the title in the window with padding
artist.move(100,40) #move the artist name in the window with padding

window.resize(350, 80) #to resizing the window size

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

#to display the ui of the window
window.show()

app.exec()