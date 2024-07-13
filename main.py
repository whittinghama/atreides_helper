from PyQt6.QtWidgets import QApplication
from mainWindow import MainWindow

app = QApplication([])

window = MainWindow()
window.show()

app.exec()