from PyQt6.QtWidgets import QVBoxLayout, QGridLayout, QPlainTextEdit, QLabel, QPushButton
from PyQt6.QtCore import Qt, pyqtSignal

from maps import cardMap
from menus import DiscardMenu

class FactionLayout(QVBoxLayout):

    def __init__(self, faction: str):
        super().__init__()
        
        self.faction = faction
        self.cardsHeld = 0

        self.titleLabel = QLabel(faction)
        titleFont = self.titleLabel.font()

        titleFont.setBold(True)
        titleFont.setPointSize(20)

        self.titleLabel.setFont(titleFont)
        
        self.numCards =  8 if faction == "Harkonnen" else 4
        self.cards = ["tcard_none"] * self.numCards
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

        self.discardButton = QPushButton("Discard")
        self.discardMenu = DiscardMenu(self.discardButton, self.numCards)
        self.discardButton.setMenu(self.discardMenu)
        self.discardMenu.triggered.connect(self.discardMenuTriggered)

        self.addWidget(self.discardButton)

        self.addWidget(QPlainTextEdit())

    def assignCard(self, card: str):
        for i in range(self.numCards):
            if self.cardLabels[i].text() != "No Card":
                continue
            else:
                self.cardLabels[i].setText(cardMap[card])
                self.cards[i] = card
                self.cardsHeld += 1
                break

    def discardMenuTriggered(self, action):
        cardNum = action.data()
        self.cards[cardNum] = "tcard_none"
        self.cardLabels[cardNum].setText("No Card")
        self.cardsHeld -= 1
