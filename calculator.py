import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QGridLayout
)

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(300, 300, 320, 450)

        layout = QVBoxLayout()

        # Display
        self.display = QLineEdit()
        self.display.setFixedHeight(80)
        self.display.setStyleSheet("font-size: 28px;")
        layout.addWidget(self.display)

        # Buttons
        grid = QGridLayout()

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 0
        col = 0

        for button in buttons:
            btn = QPushButton(button)
            btn.setFixedHeight(50)
            btn.clicked.connect(self.button_clicked)

            grid.addWidget(btn, row, col)

            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addLayout(grid)

        # Clear Button
        clear_btn = QPushButton("C")
        clear_btn.setFixedHeight(50)
        clear_btn.clicked.connect(self.display.clear)

        layout.addWidget(clear_btn)

        self.setLayout(layout)

    def button_clicked(self):
        button = self.sender().text()

        if button == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + button)


app = QApplication(sys.argv)

window = Calculator()
window.show()

sys.exit(app.exec_())