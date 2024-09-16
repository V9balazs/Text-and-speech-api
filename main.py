import sys
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

from PyQt6 import QtWidgets

from view import MainView

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainView()
    window.show()
    sys.exit(app.exec())
