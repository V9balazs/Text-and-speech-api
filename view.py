from elevenlabs import voices
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QThread, QUrl, pyqtSignal
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer

from elevenlabs_api_call import avaliable_voices, text_to_speech
from openai_api_call import text_to_speech


class MainView(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("MainView.ui", self)

        self.pushButton.clicked.connect(self.button_clicked)
        self.comboBox.currentTextChanged.connect(self.combo_changed)
        self.comboBox_2.currentTextChanged.connect(self.combo_changed)
        self.textEdit.textChanged.connect(self.text_changed)

        self.populate_voices_combobox()

    def button_clicked(self):
        # text = self.textEdit.toPlainText()
        # selected_index = self.comboBox.currentIndex()
        # selected_voice_id = self.comboBox.itemData(selected_index)
        # text_to_speech(text, selected_voice_id)
        text_to_speech()

    def populate_voices_combobox(self):
        voices = avaliable_voices()
        sorted_voices = sorted(voices.voices, key=lambda x: x.name)
        for voice in sorted_voices:
            self.comboBox.addItem(voice.name, userData=voice.voice_id)

    def combo_changed(self):
        pass

    def text_changed(self):
        pass
