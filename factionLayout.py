from PyQt6.QtWidgets import QVBoxLayout, QGridLayout, QPlainTextEdit, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRect, Qt

from cardLayout import CardLayout
from maps import cardMap

class FactionLayout(QVBoxLayout):

    def __init__(self, faction: str):
        super().__init__()
        
        self.faction = faction

        self.titleLabel = QLabel(faction)
        titleFont = self.titleLabel.font()

        titleFont.setBold(True)
        titleFont.setPointSize(24)

        self.titleLabel.setFont(titleFont)
        
        self.numCards =  8 if faction == "Harkonnen" else 4
        self.cardLabels = []
        self.cardGridLayout = QGridLayout()
        
        self.addWidget(self.titleLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        for i in range(self.numCards):
            leftLabel = QLabel(f"Card {i+1}:")
            label = QLabel("No Card")
            self.cardLabels.append(label)
            self.cardGridLayout.addWidget(leftLabel, i, 0, alignment=Qt.AlignmentFlag.AlignRight)
            self.cardGridLayout.addWidget(self.cardLabels[i], i, 1, alignment=Qt.AlignmentFlag.AlignLeft)

        self.addLayout(self.cardGridLayout)
        
        self.addWidget(QPlainTextEdit())

    def assignCard(self, card: str):
        for i in range(self.numCards):
            if self.cardLabels[i].text() != "No Card":
                continue
            else:
                self.cardLabels[i].setText(cardMap[card])
                break
