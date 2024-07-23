from PyQt6.QtCore import QRect, Qt, pyqtSignal
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QMenu
from PyQt6.QtGui import QAction, QPixmap

from menus import CardMenu

class CardLayout(QVBoxLayout):

    cardDrawn = pyqtSignal(str, str)

    def __init__(self, factions):
        super().__init__()
        self.setContentsMargins(0,0,0,0)

        self.currentCard = "tcard_none"

        self.selectButton = QPushButton("Select Card")
        self.selectMenu = CardMenu(self.selectButton)

        self.selectMenu.triggered.connect(self.selectMenuTriggered)

        self.selectButton.setMenu(self.selectMenu)
        self.addWidget(self.selectButton)

        self.image = QPixmap("images/tcard_none.png")

        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(self.image)
        self.addWidget(self.imageLabel)

        self.factionButton = QPushButton("Winning Bid")
        self.factionMenu = QMenu(self.factionButton)
        self.factionActions = []
        for faction in factions:
            action = QAction(faction)
            action.setData(faction)
            self.factionActions.append(action)
            
        self.factionMenu.addActions(self.factionActions)
        self.factionMenu.addSeparator()
        self.factionNoAction = QAction("No Winning Bid")
        self.factionMenu.addAction(self.factionNoAction)

        self.factionMenu.triggered.connect(self.factionMenuTriggered)
        self.factionButton.setMenu(self.factionMenu)

        self.addWidget(self.factionButton)

    def selectMenuTriggered(self, action):
        self.currentCard = action.data()
        self.image = QPixmap(f"images/{action.data()}.png")
        self.setScaledImage()        

    def factionMenuTriggered(self, action):
        self.cardDrawn.emit(self.currentCard, action.data())

    def setGeometry(self, rect: QRect) -> None:
        super().setGeometry(rect)
        self.setScaledImage()

    def setScaledImage(self):
        size = self.imageLabel.geometry().size()
        scaledImage = self.image.scaled(size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.imageLabel.setPixmap(scaledImage)
        