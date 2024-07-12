from PyQt6.QtWidgets import QHBoxLayout, QPlainTextEdit
from factionWidget import factionWidget
from cardWidget import cardWidget

class factionLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.addWidget(factionWidget())
        for _ in range(4):
            self.addWidget(cardWidget())
        self.addWidget(QPlainTextEdit())
