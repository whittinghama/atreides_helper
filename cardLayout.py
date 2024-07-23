from PyQt6.QtCore import QRect, Qt, pyqtSignal
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QMenu
from PyQt6.QtGui import QAction, QPixmap

class CardLayout(QVBoxLayout):

    cardDrawn = pyqtSignal(str, str)

    def __init__(self, factions):
        super().__init__()
        self.setContentsMargins(0,0,0,0)

        self.currentCard = "tcard_none"

        self.selectButton = QPushButton("Select Card")

        self.selectMenu = QMenu(self.selectButton)
        self.wMenu = QMenu("Weapon")
        self.dMenu = QMenu("Defence")
        self.specMenu = QMenu("Special")

        # Weapon menu actions
        self.wPoiAction = QAction("Poison")
        self.wProAction = QAction("Projectile")
        self.wLasAction = QAction("Lasgun")
        self.wPoiAction.setData("tcard_weap_poi")
        self.wProAction.setData("tcard_weap_pro")
        self.wLasAction.setData("tcard_weap_las")

        self.wMenu.addActions([self.wPoiAction, self.wProAction, self.wLasAction])

        # Defence menu actions
        self.dPoiAction = QAction("Poison")
        self.dProAction = QAction("Projectile")
        self.dPoiAction.setData("tcard_def_poi")
        self.dProAction.setData("tcard_def_pro")

        self.dMenu.addActions([self.dPoiAction, self.dProAction])

        # self.special menu actions
        self.specHeroAction = QAction("Cheap Hero")
        self.specKaraAction = QAction("Karama")
        self.specMoveAction = QAction("Hajr (movement)")
        self.specRevAction = QAction("Tleilaxu Ghola (revive)")
        self.specStormAction = QAction("Weather Control")
        self.specTruthAction = QAction("Truthtrance")
        self.specWallAction = QAction("Family Atomics")
        self.specHeroAction.setData("tcard_spec_hero")
        self.specKaraAction.setData("tcard_spec_kara")
        self.specMoveAction.setData("tcard_spec_move")
        self.specRevAction.setData("tcard_spec_rev")
        self.specStormAction.setData("tcard_spec_storm")
        self.specTruthAction.setData("tcard_spec_truth")
        self.specWallAction.setData("tcard_spec_wall")

        self.specMenu.addActions([self.specHeroAction, self.specKaraAction,self.specMoveAction, self.specRevAction, self.specStormAction, self.specTruthAction, self.specWallAction])

        # Top menu actions
        self.worthlessAction = QAction("Worthless Card")
        self.unknownAction = QAction("Unknown Card")
        self.clearAction = QAction("Clear")
        self.worthlessAction.setData("tcard_worthless")
        self.unknownAction.setData("tcard_base")
        self.clearAction.setData("tcard_none")

        self.selectMenu.addMenu(self.wMenu)
        self.selectMenu.addMenu(self.dMenu)
        self.selectMenu.addMenu(self.specMenu)
        self.selectMenu.addActions([self.worthlessAction, self.unknownAction])
        self.selectMenu.addSeparator()
        self.selectMenu.addAction(self.clearAction)

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
        