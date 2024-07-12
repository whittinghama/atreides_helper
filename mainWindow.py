from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from factionLayout import factionLayout

# Subclass QMainWindow to customize your application's main window
class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()
        for _ in range(4):
            layout.addLayout(factionLayout())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)