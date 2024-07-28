from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QGridLayout, QLineEdit, QSizePolicy
from decks import SpiceDeck

class SpiceLayout(QVBoxLayout):
    def __init__(self, enableStats : bool):
        super().__init__()
        self.statsEnabled = enableStats
        self.currentTurn = 0

        commonSizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.topLayout = QVBoxLayout()

        self.titleLabel = QLabel("Spice Cards")
        font = self.titleLabel.font()
        font.setBold(True)
        font.setPointSize(20)
        self.titleLabel.setFont(font)
        self.titleLabel.setSizePolicy(commonSizePolicy)

        self.topLayout.addWidget(self.titleLabel, alignment=(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter))

        self.deck = SpiceDeck()

        self.buttonLayout = QHBoxLayout()

        self.spiceButton = QPushButton("Spice")
        self.wormButton = QPushButton("Worm")
        self.buttonLayout.addWidget(self.spiceButton)
        self.buttonLayout.addWidget(self.wormButton)

        self.spiceButton.clicked.connect(self.drawSpice)
        self.wormButton.clicked.connect(self.drawWorm)

        self.topLayout.addLayout(self.buttonLayout)
        self.topLayout.addStretch(1)

        self.addLayout(self.topLayout)

        if self.statsEnabled:
            self.statsLayout = QGridLayout()
            self.statsTitle = QLabel("Stats")
            statsTitleFont = self.statsTitle.font()
            statsTitleFont.setBold(True)
            statsTitleFont.setPointSize(12)
            self.statsTitle.setFont(statsTitleFont)
            self.statsTitle.setSizePolicy(commonSizePolicy)
            self.statsLayout.addWidget(self.statsTitle, 0, 0, 1, 2, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop))

            self.statsLabels = {}
            row = 1
            for stat in self.deck.get_stats().keys():
                statLabelText = f"{stat}:"
                statLabel = QLabel(statLabelText)
                statLabel.setSizePolicy(commonSizePolicy)
                valueLabel = QLabel("TBD %")
                valueLabel.setSizePolicy(commonSizePolicy)

                self.statsLabels[stat] = (statLabel, valueLabel)
                self.statsLayout.addWidget(self.statsLabels[stat][0], row, 0, alignment=Qt.AlignmentFlag.AlignRight)
                self.statsLayout.addWidget(self.statsLabels[stat][1], row, 1, alignment=Qt.AlignmentFlag.AlignLeft)
                row += 1

            self.updateStats()
            self.addLayout(self.statsLayout)

        self.turnsLayout = QGridLayout()
        self.spiceLabels = []
        for i in range(10):
            turnLabel = QLabel(f"{i+1}:")
            spiceLabel = QLabel("Unknown")
            self.spiceLabels.append(spiceLabel)
            self.turnsLayout.addWidget(turnLabel, i, 0, alignment=Qt.AlignmentFlag.AlignRight)
            self.turnsLayout.addWidget(self.spiceLabels[i], i, 1, alignment=Qt.AlignmentFlag.AlignLeft)
            self.turnsLayout.addWidget(QLineEdit(), i, 2)
            self.turnsLayout.setRowStretch(i, 1)

        self.addLayout(self.turnsLayout, stretch=1)
        self.addStretch(1)

    def drawSpice(self):
        self.deck.draw_card("Spice")
        self.updateStats()
        self.spiceLabels[self.currentTurn].setText("Spice")
        self.currentTurn += 1

    def drawWorm(self):
        self.deck.draw_card("Worm")
        self.updateStats()
        self.spiceLabels[self.currentTurn].setText("Worm")
        self.currentTurn += 1

    def updateStats(self):
        stats = self.deck.get_stats()
        for stat, value in stats.items():
            valueLabelText = f"{value:5.2f} %"
            self.statsLabels[stat][1].setText(valueLabelText)