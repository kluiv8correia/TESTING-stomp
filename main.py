import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Simple PyQt5 App")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        label = QLabel("Created in develop v1.0-alpha")
        layout.addWidget(label)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleApp()
    window.show()
    sys.exit(app.exec_())
