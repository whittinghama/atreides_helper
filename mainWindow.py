from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from PyQt6.QtGui import QIcon

from factionLayout import FactionLayout

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Atreides Helper")
        self.setWindowIcon(QIcon("images/atr_logo_256x.png"))

        layout = QVBoxLayout()
        for _ in range(4):
            layout.addLayout(FactionLayout())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)