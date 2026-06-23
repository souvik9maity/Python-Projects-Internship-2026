import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Online Quiz Platform")
        self.setFixedSize(550, 400)

        self.questions = [
            {
                "question": "Which data structure follows FIFO?",
                "options": ["Stack", "Queue", "Tree", "Graph"],
                "answer": "Queue"
            },
            {
                "question": "Which language is primarily used for AI and Machine Learning?",
                "options": ["Python", "HTML", "CSS", "SQL"],
                "answer": "Python"
            },
            {
                "question": "Which company developed Windows Operating System?",
                "options": ["Google", "Apple", "Microsoft", "Intel"],
                "answer": "Microsoft"
            },
            {
                "question": "What does CPU stand for?",
                "options": [
                    "Central Processing Unit",
                    "Computer Processing Unit",
                    "Central Program Utility",
                    "Control Processing Unit"
                ],
                "answer": "Central Processing Unit"
            },
            {
                "question": "Which language is used for database queries?",
                "options": ["Python", "Java", "SQL", "C++"],
                "answer": "SQL"
            }
        ]

        self.index = 0
        self.score = 0

        layout = QVBoxLayout()

        self.score_label = QLabel("Score: 0")
        self.score_label.setStyleSheet(
            "font-size:16px; font-weight:bold;"
        )
        layout.addWidget(self.score_label)

        self.question_label = QLabel("")
        self.question_label.setWordWrap(True)
        self.question_label.setStyleSheet(
            "font-size:18px; font-weight:bold; padding:10px;"
        )
        layout.addWidget(self.question_label)

        self.buttons = []

        for i in range(4):
            btn = QPushButton()
            btn.setMinimumHeight(45)
            btn.clicked.connect(self.check_answer)
            self.buttons.append(btn)
            layout.addWidget(btn)

        self.setLayout(layout)

        self.load_question()

    def load_question(self):
        q = self.questions[self.index]

        self.question_label.setText(
            f"Question {self.index + 1}/{len(self.questions)}\n\n{q['question']}"
        )

        for i in range(4):
            self.buttons[i].setText(q["options"][i])

    def check_answer(self):
        selected = self.sender().text()
        correct_answer = self.questions[self.index]["answer"]

        if selected == correct_answer:
            self.score += 1

        else:
            QMessageBox.information(
                self,
                "Wrong Answer",
                f"❌ Wrong Answer\n\nCorrect Answer: {correct_answer}"
            )

        self.score_label.setText(f"Score: {self.score}")

        self.index += 1

        if self.index < len(self.questions):
            self.load_question()

        else:
            percentage = (self.score / len(self.questions)) * 100

            QMessageBox.information(
                self,
                "Quiz Result",
                f"Final Score: {self.score}/{len(self.questions)}\n"
                f"Percentage: {percentage:.0f}%"
            )

            self.close()


app = QApplication(sys.argv)

window = QuizApp()
window.show()

sys.exit(app.exec_())