from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPlainTextEdit, QPushButton
from cardLayout import CardLayout

class FactionWidget(QWidget):
    def __init__(self):
        super().__init__()
  

class FactionLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.addWidget(FactionWidget())
        for _ in range(4):
            self.addLayout(CardLayout())
        self.addWidget(QPlainTextEdit())
