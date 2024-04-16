from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QFileDialog
class Importer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Drop or click 'Import' to select a file.", self)
        self.label.setFixedSize(400, 100)
        self.label.setStyleSheet("border: 2px dashed #aaa; font-size: 16px; text-align: center;")
        layout.addWidget(self.label)

        self.btn_import = QPushButton('Import', self)
        self.btn_import.clicked.connect(self.openFileNameDialog)
        layout.addWidget(self.btn_import)

        self.error_display = QTextEdit(self)
        self.error_display.setReadOnly(True)
        self.error_display.setPlaceholderText("Data errors will be displayed here.")
        self.error_display.setFixedSize(400, 100)
        layout.addWidget(self.error_display)

        self.setLayout(layout)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if fileName:
            self.processFile(fileName)

    def processFile(self, filePath):
        self.label.setText(f"File loaded: {filePath}")
        try:
            with open(filePath, 'r') as file:
                data = json.load(file)
                self.error_display.setText("JSON loaded successfully:\n" + json.dumps(data, indent=4))
        except json.JSONDecodeError as e:
            self.error_display.setText(f"JSON Decode Error: {e}")
        except Exception as e:
            self.error_display.setText(f"Error: {e}")
