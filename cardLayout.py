from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QMenu
from PyQt6.QtGui import QAction, QPixmap


class CardLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Select Card")

        self.topMenu = QMenu(self.button)
        self.wMenu = QMenu("Weapon")
        self.dMenu = QMenu("Defence")
        self.specMenu = QMenu("Special")

        # Weapon menu actions
        self.wPoiAction = QAction("Poison")
        self.wProAction = QAction("Projectile")
        self.wLasAction = QAction("Lasgun")

        self.wMenu.addActions([self.wPoiAction, self.wProAction, self.wLasAction])

        # Defence menu actions
        self.dPoiAction = QAction("Poison")
        self.dProAction = QAction("Projectile")

        self.dMenu.addActions([self.dPoiAction, self.dProAction])

        # self.special menu actions
        self.specHeroAction = QAction("Cheap Hero")
        self.specKaraAction = QAction("Karama")
        self.specMoveAction = QAction("Hajr (movement)")
        self.specRevAction = QAction("Tleilaxu Ghola (revive)")
        self.specStormAction = QAction("Weather Control")
        self.specTruthAction = QAction("Truthtrance")
        self.specWallAction = QAction("Family Atomics")

        self.specMenu.addActions([self.specHeroAction, self.specKaraAction,self.specMoveAction, self.specRevAction, self.specStormAction, self.specTruthAction, self.specWallAction])

        # Top menu actions
        self.worthlessAction = QAction("Worthless Card")
        self.unknownAction = QAction("Unknown Card")
        self.clearAction = QAction("Clear")

        self.topMenu.addMenu(self.wMenu)
        self.topMenu.addMenu(self.dMenu)
        self.topMenu.addMenu(self.specMenu)
        self.topMenu.addActions([self.worthlessAction, self.unknownAction])
        self.topMenu.addSeparator()
        self.topMenu.addAction(self.clearAction)

        self.topMenu.triggered.connect(self.menuTriggered)

        self.button.setMenu(self.topMenu)
        self.addWidget(self.button)


        self.image = QLabel()
        self.image.setPixmap(QPixmap("images/tcard_none.png"))
        self.addWidget(self.image)

    def menuTriggered(self, action):
        print(super().geometry().height())