import sys
import subprocess
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel,
    QLineEdit, QPushButton, QFileDialog,
    QVBoxLayout, QMessageBox
)


class ModelRunner(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenModelica Runner")
        self.setGeometry(200, 200, 400, 250)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Select executable
        self.file_label = QLabel("Select Executable:")
        self.file_input = QLineEdit()
        self.browse_btn = QPushButton("Browse")

        # Start time
        self.start_label = QLabel("Start Time:")
        self.start_input = QLineEdit()

        # Stop time
        self.stop_label = QLabel("Stop Time:")
        self.stop_input = QLineEdit()

        # Run button
        self.run_btn = QPushButton("Run Simulation")

        # Add widgets
        layout.addWidget(self.file_label)
        layout.addWidget(self.file_input)
        layout.addWidget(self.browse_btn)
        layout.addWidget(self.start_label)
        layout.addWidget(self.start_input)
        layout.addWidget(self.stop_label)
        layout.addWidget(self.stop_input)
        layout.addWidget(self.run_btn)

        self.setLayout(layout)

        # Connect buttons
        self.browse_btn.clicked.connect(self.browse_file)
        self.run_btn.clicked.connect(self.run_model)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Executable",
            "",
            "Executable Files (*.exe)"
        )
        if file_path:
            self.file_input.setText(file_path)

    def run_model(self):
        exe_path = self.file_input.text()
        start_time = self.start_input.text()
        stop_time = self.stop_input.text()

        # Validation
        try:
            start = int(start_time)
            stop = int(stop_time)

            if not (0 <= start < stop < 5):
                QMessageBox.warning(
                    self,
                    "Invalid Input",
                    "Condition: 0 ≤ start < stop < 5"
                )
                return

        except ValueError:
            QMessageBox.warning(
                self,
                "Invalid Input",
                "Start and Stop time must be integers"
            )
            return

        # Command
        command = [
            exe_path,
            f"-override=startTime={start},stopTime={stop}"
        ]

        # Run simulation
        try:
            subprocess.run(
    command,
    cwd=os.path.dirname(exe_path),
    capture_output=True,
    text=True
)

            QMessageBox.information(
                self,
                "Success",
                "Simulation executed successfully"
            )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModelRunner()
    window.show()
    sys.exit(app.exec())