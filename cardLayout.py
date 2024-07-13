from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMenu, QLabel
from PyQt6.QtGui import QAction

class CardButton(QWidget):
    def __init__(self):
        super().__init__()

        topMenu = QMenu()
        wMenu = QMenu("Weapon")
        dMenu = QMenu("Defence")
        specMenu = QMenu("Special")

        # Weapon menu actions
        wPoiAction = QAction("Poison")
        wProAction = QAction("Projectile")
        wLasAction = QAction("Lasgun")

        wMenu.addActions([wPoiAction, wProAction, wLasAction])

        # Defence menu actions
        dPoiAction = QAction("Poison")
        dProAction = QAction("Projectile")

        dMenu.addActions([dPoiAction, dProAction])

        # Special menu actions
        specHeroAction = QAction("Cheap Hero")
        specKaraAction = QAction("Karama")
        specMoveAction = QAction("Hajr (movement)")
        specRevAction = QAction("Tleilaxu Ghola (revive)")
        specStormAction = QAction("Weather Control")
        specTruthAction = QAction("Truthtrance")
        specWallAction = QAction("Family Atomics")

        specMenu.addActions([specHeroAction, specKaraAction,specMoveAction, specRevAction, specStormAction, specTruthAction, specWallAction])

        # Top menu actions
        worthlessAction = QAction("Worthless Card")
        unknownAction = QAction("Unknown Card")
        clearAction = QAction("Clear")

        topMenu.addMenu(wMenu)
        topMenu.addMenu(dMenu)
        topMenu.addMenu(specMenu)
        topMenu.addActions([worthlessAction, unknownAction])
        topMenu.addSeparator()
        topMenu.addAction(clearAction)

        button = QPushButton("Select Card")
        button.setMenu(topMenu)

class CardLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.addWidget(CardButton())
        self.addWidget(QLabel("placeholder"))