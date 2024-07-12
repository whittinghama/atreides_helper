from PyQt6.QtWidgets import QApplication
from mainWindow import mainWindow

app = QApplication([])

window = mainWindow()
window.show()

app.exec()