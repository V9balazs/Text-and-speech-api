import os
import sys
import uuid
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

from dotenv import load_dotenv
from elevenlabs import VoiceSettings, play
from elevenlabs.client import ElevenLabs
from PyQt6 import QtWidgets

from view import MainView

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainView()
    window.show()
    sys.exit(app.exec())
