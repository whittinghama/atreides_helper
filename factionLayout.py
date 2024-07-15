from PyQt6.QtWidgets import QHBoxLayout, QPlainTextEdit, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QRect, Qt

from cardLayout import CardLayout


class FactionLayout(QHBoxLayout):
    def __init__(self, faction: str):
        super().__init__()
        
        self.image = QPixmap(f"images/{faction}.png")
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(self.image)
        
        self.addWidget(self.imageLabel)
        numCards =  8 if faction == "Harkonnen" else 4
        for _ in range(numCards):
            self.addLayout(CardLayout())
        self.addWidget(QPlainTextEdit())

        self.setScaledImage()

    def setGeometry(self, rect: QRect) -> None:
        super().setGeometry(rect)
        self.setScaledImage()

    def setScaledImage(self):
        size = self.imageLabel.geometry().size()
        scaledImage = self.image.scaled(size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.imageLabel.setPixmap(scaledImage)
