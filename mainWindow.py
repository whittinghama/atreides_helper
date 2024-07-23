from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QDialogButtonBox, QHBoxLayout, QDialog, QCheckBox
from PyQt6.QtGui import QIcon, QResizeEvent
from PyQt6.QtCore import Qt

from factionLayout import FactionLayout
from bidLayout import BidLayout
from decks import TreacheryDeck


class FactionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Factions")
        self.setWindowIcon(QIcon("images/atr_logo_256x"))

        self.layout = QVBoxLayout()

        self.factionBoxes = [QCheckBox("Bene Gesserit"), QCheckBox("Emperor"), QCheckBox("Fremen"), QCheckBox("Harkonnen"), QCheckBox("Spacing Guild")]
        for box in self.factionBoxes:
            self.layout.addWidget(box)

        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        self.layout.addWidget(self.buttons)

        self.setLayout(self.layout)


class MainWindow(QMainWindow):

    deck = TreacheryDeck()

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Atreides Helper")
        self.setWindowIcon(QIcon("images/atr_logo_256x.png"))

        dlg = FactionDialog(self)

        factionStrings = []
        self.factionLayouts = {}

        if dlg.exec():
            for box in dlg.factionBoxes:
                if box.isChecked():
                    factionStrings.append(box.text())
        else:
            exit()

        layout = QVBoxLayout()
        allFactions = QHBoxLayout()

        self.bidLayout = BidLayout(factionStrings)
        self.bidLayout.cardDrawn.connect(self.assignCard)
        layout.addLayout(self.bidLayout)

        for faction in factionStrings:
            self.factionLayouts[faction] = FactionLayout(faction)
            allFactions.addLayout(self.factionLayouts[faction])

        layout.addLayout(allFactions)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def assignCard(self, card: str, faction: str):
        if card == "tcard_base":
            self.deck.draw_card(False)
        else:
            self.deck.draw_card(True, card)

        if faction:
            self.factionLayouts[faction].assignCard(card)
        else:
            self.deck.discard_card(card)