from random import choice, shuffle
from PyQt5.QtWidgets import QApplication

app = QApplication([])

from memo___card_layout import *
from memo_menu import *

class Question:
    def init(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()

def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                cur_q.got_right()
                lb_result.setText('Вірно!')
                answer.setChecked(False)
                break
    else:
        lb_result.setText('Не вірно!')
        cur_q.got_wrong()

    RadioGroup.setExclusive(True)

def click_ok():
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()

        btn_next.setText('Наступне запитання')
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()

        btn_next.setText('Відповісти')
def SetMenu():
    lb_statistic.setText(str(cur_q.count_right))
    menu_win.show()
    window.hide()
def SetMain():
    window.show()
    menu_win.hide()

def AddQuestion():
    t =le_question.text()
    ra = le_right_ans.text()
    wa1 = le_wrong_ans1.text()
    wa2 = le_wrong_ans2.text()

    wa3 = le_wrong_ans3.text()

    question = Question(t,ra,wa1,wa2,wa3)
    questions.append(question)
    ClearLines()
def ClearLines():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_next.clicked.connect(click_ok)
btn_menu.clicked.connect(SetMenu)
btn_back.clicked.connect(SetMain)
btn_add_question.clicked.connect(AddQuestion)
btn_clear.clicked.connect(ClearLines)
window.setLayout(vl_res)
window.show()
app.exec_()