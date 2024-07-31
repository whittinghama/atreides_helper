from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QHBoxLayout

from cardLayout import CardLayout
from spiceLayout import SpiceLayout

class BidLayout(QHBoxLayout):

    cardDrawn = pyqtSignal(str, str)

    def __init__(self, factions):
        super().__init__()

        self.spiceLayout = SpiceLayout()
        self.addLayout(self.spiceLayout)
        
        self.cardLayouts = []
        
        for i in range(len(factions)):
            self.cardLayouts.append(CardLayout(factions))
            self.addLayout(self.cardLayouts[i])
            self.cardLayouts[i].cardDrawn.connect(self.cardDrawn)
