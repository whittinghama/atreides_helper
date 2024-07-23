from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QHBoxLayout, QLabel
from PyQt6.QtGui import QAction, QPixmap

from cardLayout import CardLayout

class BidLayout(QHBoxLayout):

    cardDrawn = pyqtSignal(str, str)

    def __init__(self, factions):
        super().__init__()

        self.cardLayouts = []

        for i in range(5):
            self.cardLayouts.append(CardLayout(factions))
            self.addLayout(self.cardLayouts[i])
            self.cardLayouts[i].cardDrawn.connect(self.cardDrawn)
        
    def relayCardDrawn(self, card: str, faction: str):
        self.cardDrawn.emit(card, faction)
    