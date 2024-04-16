import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication
from importer import Importer
from runner import Runner
from plotter import Plotter

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        h_layout = QHBoxLayout(self)

        self.importer = Importer()
        self.runner = Runner()
        self.plotter = Plotter()

        h_layout.addWidget(self.importer)
        h_layout.addWidget(self.runner)
        h_layout.addWidget(self.plotter)

        self.setLayout(h_layout)
        self.setWindowTitle('PyQt5 Application')
        self.setGeometry(300, 300, 1280, 300)

def main():
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()