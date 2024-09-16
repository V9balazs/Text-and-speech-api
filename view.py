from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QThread, pyqtSignal


class MainView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MainView.ui", self)

        self.pushButton.clicked.connect(self.button_clicked)
        self.comboBox.currentTextChanged.connect(self.combo_changed)
        self.textEdit.textChanged.connect(self.text_changed)

    def button_clicked(self):
        print("Gomb megnyomva")

    def combo_changed(self):
        print("Combo box változott")

    def text_changed(self):
        print("Szöveg változott")
