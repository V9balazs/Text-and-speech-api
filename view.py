from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QThread, pyqtSignal

from api_call import text_to_speech


class MainView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MainView.ui", self)

        self.pushButton.clicked.connect(self.button_clicked)
        self.comboBox.currentTextChanged.connect(self.combo_changed)
        self.textEdit.textChanged.connect(self.text_changed)

    def button_clicked(self):
        text = self.textEdit.toPlainText()
        text_to_speech(text)

    def combo_changed(self):
        print("Combo box változott")

    def text_changed(self):
        pass
