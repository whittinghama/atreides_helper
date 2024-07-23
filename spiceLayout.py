from PyQt6.QtCore import QRect, Qt, pyqtSignal
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QMenu
from PyQt6.QtGui import QAction, QPixmap

from decks import SpiceDeck

class SpiceLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()