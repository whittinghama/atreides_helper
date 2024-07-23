from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel

from cardLayout import CardLayout
from spiceLayout import SpiceLayout

class BidLayout(QHBoxLayout):

    cardDrawn = pyqtSignal(str, str)

    def __init__(self, factions, statsKeys):
        super().__init__()

        self.cardLayouts = []
        self.statsLayout = QVBoxLayout()

        for i in range(5):
            self.cardLayouts.append(CardLayout(factions))
            self.addLayout(self.cardLayouts[i])
            self.cardLayouts[i].cardDrawn.connect(self.cardDrawn)

        self.statsTitle = QLabel("Stats")
        statsTitleFont = self.statsTitle.font()
        statsTitleFont.setBold(True)
        statsTitleFont.setPointSize(14)
        self.statsTitle.setFont(statsTitleFont)
        self.statsLayout.addWidget(self.statsTitle, Qt.AlignmentFlag.AlignCenter)

        self.statsLabels = {}
        for stat in statsKeys:
            labelText = f"{stat}: Unknown"
            label = QLabel(labelText)
            self.statsLabels[stat] = label
            self.statsLayout.addWidget(self.statsLabels[stat], Qt.AlignmentFlag.AlignCenter)  

        self.addLayout(self.statsLayout)
        
    def updateStats(self, stats: dict):
        for stat, value in stats.items():
            labelText = f"{stat}: {value}"
            self.statsLabels[stat].setText(labelText)