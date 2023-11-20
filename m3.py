from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout,QPushButton,QLabel
menu_win = QWidget()
lb_quest = QLabel("Введіть запитання:")
lb_wrong_ans = QLabel("Введіть правильну відповідь:")
lb_wrong_ans1 = QLabel("Введіть першу неправильну відповідь:")
lb_wrong_ans2 = QLabel("Введіть другу неправильну відповідь:")
lb_wrong_ans3=QLabel("Введіть третю неправильну відповідь:")
le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1= QLineEdit()
le_wrong_ans2= QLineEdit()
le_wrong_ans3= QLineEdit()
lb_header_stat = QLabel("Статистика")
le_statistic = QLabel()
v1_lables= QVBoxLayout()
v1_lables.addWidget(lb_quest)
v1_lables.addWidget(le_right_ans)
v1_lables.addWidget(le_wrong_ans1)
v1_lables.addWidget(lb_wrong_ans2)
v1_lables.addWidget(lb_wrong_ans3)

v1_LineEdits= QVBoxLayout()
v1_LineEdits.addWidget(le_question)
v1_LineEdits.addWidget(le_right_ans)
v1_LineEdits.addWidget(le_wrong_ans1)
v1_LineEdits.addWidget(lb_wrong_ans2)
v1_LineEdits.addWidget(lb_wrong_ans3)

h1_question = QHBoxLayout()
h1_question.addLayout(v1_lables)
h1_question.addLayout(v1_LineEdits)

btn_back = QPushButton("Назад")
btn_add_question = QPushButton("Додати")
btn_clear = QPushButton("Очистити")
h1_buttons = QHBoxLayout()
h1_buttons.addWidget(btn_add_question)
h1_buttons.addWidget(btn_clear)

v1_res= QVBoxLayout()
v1_res.addLayout(h1_question)
v1_res.addLayout(h1_buttons)
v1_res.addWidget(lb_header_stat)
v1_res.addWidget(btn_back)
menu_win.setLayout(v1_res)
menu_win.resize(400,500)