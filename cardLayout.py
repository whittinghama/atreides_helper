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
        self.image.setPixmap(QPixmap(f"images/{action.data()}.png"))