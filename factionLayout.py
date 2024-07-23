from PyQt6.QtWidgets import QVBoxLayout, QFormLayout, QPlainTextEdit, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import QRect, Qt

from cardLayout import CardLayout


class FactionLayout(QVBoxLayout):

    cardMap = {"tcard_weap_poi" : "Weapon - Poison",
               "tcard_weap_pro" : "Weapon - Projectile",
               "tcard_weap_las" : "Weapon - Lasgun",
               "tcard_def_poi" : "Defence - Poison",
               "tcard_def_pro" : "Defence - Projectile",
               "tcard_spec_kara" : "Special - Karama",
               "tcard_spec_hero" : "Special - Hero",
               "tcard_spec_move" : "Special - Hajr (Move)",
               "tcard_spec_rev" : "Special - Revive",
               "tcard_spec_storm" : "Special - Storm",
               "tcard_spec_truth" : "Special - Truthtrance",
               "tcard_spec_wall" : "Special - Wall bomb",
               "tcard_worthless" : "Worthless",
               "tcard_base" : "Unknown card"}

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
        self.cardFormLayout = QFormLayout()
        
        self.addWidget(self.titleLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        for i in range(self.numCards):
            label = QLabel("No Card")
            self.cardLabels.append(label)
            self.cardFormLayout.addRow(f"Card {i+1}", self.cardLabels[i])

        self.addLayout(self.cardFormLayout)
        
        self.addWidget(QPlainTextEdit())

    def assignCard(self, card: str):
        print(f"{self.faction}: Drawn {self.cardMap[card]}")
        for i in range(self.numCards):
            if self.cardLabels[i].text() != "No Card":
                continue
            else:
                self.cardLabels[i].setText(self.cardMap[card])
                break
