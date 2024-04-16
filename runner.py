from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit

class Runner(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.btn_run = QPushButton('Run', self)
        self.btn_run.clicked.connect(self.runCode)
        layout.addWidget(self.btn_run)

        self.runtime_errors = QTextEdit(self)
        self.runtime_errors.setReadOnly(True)
        self.runtime_errors.setPlaceholderText("Runtime errors will be displayed here.")
        self.runtime_errors.setFixedSize(400, 100)
        layout.addWidget(self.runtime_errors)

        self.setLayout(layout)

    def runCode(self):
        try:
            # Simulated successful or failing code execution
            self.runtime_errors.setText("Code executed successfully.")
        except Exception as e:
            self.runtime_errors.setText(f"Runtime Error: {e}")
