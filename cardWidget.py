from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPalette, QColor #temp

class cardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor('red'))
        self.setPalette(palette)    
