from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Plotter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.btn_show = QPushButton('Show', self)
        self.btn_show.clicked.connect(self.plotData)
        layout.addWidget(self.btn_show)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setFixedSize(480, 240)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def plotData(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot([0, 1, 2, 3], [10, 20, 10, 20], 'r')  # Example plot
        ax.set_title('Example Plot')
        self.canvas.draw()
