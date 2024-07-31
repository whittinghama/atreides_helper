from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QDialogButtonBox, QHBoxLayout, QDialog, QCheckBox, QPushButton, QLabel, QMessageBox
from PyQt6.QtGui import QIcon

from factionLayout import FactionLayout
from bidLayout import BidLayout
from menus import CardMenu
from maps import cardMap

class FactionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Factions")
        self.setWindowIcon(QIcon("images/atr_logo_256x"))

        self.layout = QVBoxLayout()

        self.factionBoxes = [QCheckBox("Bene Gesserit"), QCheckBox("Emperor"), QCheckBox("Fremen"), QCheckBox("Harkonnen"), QCheckBox("Spacing Guild")]
        for box in self.factionBoxes:
            self.layout.addWidget(box)

        self.cardButton = QPushButton("Select Card")
        self.cardMenu = CardMenu(self.cardButton)
        self.cardButton.setMenu(self.cardMenu)
        self.cardLabel = QLabel("Choose your starting card")
        self.cardMenu.triggered.connect(self.cardMenuTriggered)
        self.ownCard = "tcard_none"

        self.layout.addWidget(self.cardButton)
        self.layout.addWidget(self.cardLabel)

        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        self.layout.addWidget(self.buttons)

        self.setLayout(self.layout)

    def cardMenuTriggered(self, action):
        self.cardLabel.setText(cardMap[action.data()])
        self.ownCard = action.data()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Atreides Helper")
        self.setWindowIcon(QIcon("images/atr_logo_256x.png"))

        dlg = FactionDialog(self)

        factionStrings = ["Atreides"]
        self.factionLayouts = {}

        if dlg.exec():
            for box in dlg.factionBoxes:
                if box.isChecked():
                    factionStrings.append(box.text())
        else:
            exit()

        layout = QVBoxLayout()
        allFactions = QHBoxLayout()

        for faction in factionStrings:
            self.factionLayouts[faction] = FactionLayout(faction)
            allFactions.addLayout(self.factionLayouts[faction])

        self.bidLayout = BidLayout(factionStrings)
        self.bidLayout.cardDrawn.connect(self.assignCard)
        self.initialCardAssignment(factionStrings, dlg.ownCard)

        layout.addLayout(self.bidLayout)
        layout.addLayout(allFactions)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def initialCardAssignment(self, factionStrings, ownCard):
        for faction in factionStrings:
            if faction == "Atreides":
                self.assignCard(ownCard, faction)
            elif faction == "Harkonnen":
                self.factionLayouts[faction].assignCard("tcard_base")
            else:
                self.assignCard("tcard_base", faction)

    def assignCard(self, card: str, faction: str):
        if faction:
            self.factionLayouts[faction].assignCard(card)
            if faction == "Harkonnen" and self.factionLayouts[faction].cardsHeld < 8:
                self.factionLayouts[faction].assignCard("tcard_base")