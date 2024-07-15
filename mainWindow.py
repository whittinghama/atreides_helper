from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QDialogButtonBox, QFormLayout, QDialog, QCheckBox
from PyQt6.QtGui import QIcon, QResizeEvent
from PyQt6.QtCore import Qt

from factionLayout import FactionLayout


class FactionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Factions")
        self.setWindowIcon(QIcon("images/atr_logo_256x"))

        self.layout = QVBoxLayout()

        self.factionBoxes = [QCheckBox("Bene Gesserit"), QCheckBox("Emperor"), QCheckBox("Fremen"), QCheckBox("Harkonnen"), QCheckBox("Spacing Guild")]
        for box in self.factionBoxes:
            self.layout.addWidget(box)

        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        self.layout.addWidget(self.buttons)

        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Atreides Helper")
        self.setWindowIcon(QIcon("images/atr_logo_256x.png"))

        dlg = FactionDialog(self)

        factions = []
        if dlg.exec():
            for box in dlg.factionBoxes:
                if box.isChecked():
                    factions.append(box.text())
        else:
            exit()

        layout = QVBoxLayout()
        for faction in factions:
            layout.addLayout(FactionLayout(faction))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def resizeEvent(self, a0: QResizeEvent | None) -> None:
        if not self.isMinimized():
            self.showMaximized()