from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QHBoxLayout, QGridLayout, QLabel

from cardLayout import CardLayout
from spiceLayout import SpiceLayout

class BidLayout(QHBoxLayout):

    cardDrawn = pyqtSignal(str, str)

    def __init__(self, factions, statsKeys):
        super().__init__()
        if statsKeys != None:
            self.statsEnabled = True
        else:
            self.statsEnabled = False

        self.spiceLayout = SpiceLayout(self.statsEnabled)
        self.addLayout(self.spiceLayout)
        
        self.cardLayouts = []
        
        for i in range(5):
            self.cardLayouts.append(CardLayout(factions))
            self.addLayout(self.cardLayouts[i])
            self.cardLayouts[i].cardDrawn.connect(self.cardDrawn)

        if self.statsEnabled:
            self.statsLayout = QGridLayout()
            self.statsTitle = QLabel("Stats")
            statsTitleFont = self.statsTitle.font()
            statsTitleFont.setBold(True)
            statsTitleFont.setPointSize(14)
            self.statsTitle.setFont(statsTitleFont)
            self.statsLayout.addWidget(self.statsTitle, 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)

            self.statsLabels = {}
            row = 1
            for stat in statsKeys:
                statLabelText = f"{stat}:"
                statLabel = QLabel(statLabelText)
                valueLabel = QLabel("TBD %")

                self.statsLabels[stat] = (statLabel, valueLabel)
                self.statsLayout.addWidget(self.statsLabels[stat][0], row, 0, alignment=Qt.AlignmentFlag.AlignRight)
                self.statsLayout.addWidget(self.statsLabels[stat][1], row, 1, alignment=Qt.AlignmentFlag.AlignLeft)
                row += 1

            self.addLayout(self.statsLayout)
        
    def updateStats(self, stats: dict):
        if self.statsEnabled:
            for stat, value in stats.items():
                if stat == "Remaining Cards" or stat == "Unknown Cards":
                    valueLabelText = f"{value}"
                else:
                    valueLabelText = f"{value:5.2f} %"
                self.statsLabels[stat][1].setText(valueLabelText)