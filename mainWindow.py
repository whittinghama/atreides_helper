from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from factionLayout import FactionLayout

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Atreides Helper")

        layout = QVBoxLayout()
        for _ in range(4):
            layout.addLayout(FactionLayout())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)