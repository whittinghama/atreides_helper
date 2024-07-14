from PyQt6.QtWidgets import QHBoxLayout, QPlainTextEdit, QLabel
from PyQt6.QtGui import QPixmap

from cardLayout import CardLayout


class FactionLayout(QHBoxLayout):
    def __init__(self, faction: str):
        super().__init__()

        self.image = QLabel()
        self.image.setPixmap(QPixmap(f"images/{faction}.png"))

        self.addWidget(self.image)
        for _ in range(4):
            self.addLayout(CardLayout())
        self.addWidget(QPlainTextEdit())
