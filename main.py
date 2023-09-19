from PyQt6.QtWidgets import QApplication, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout

def get_a():
    try:
        global a
        a = float(input_prompt.text())
        input_prompt.clear()
    except:
        pass

def get_b():
    try:
        global b
        b = float(input_prompt.text())
        input_prompt.clear()
    except:
        pass

def get_c():
    try:
        global c
        c = float(input_prompt.text())
        input_prompt.clear()
    except:
        pass

def get_d():
    try:
        global d
        d = float(input_prompt.text())
        input_prompt.clear()
    except:
        pass

def get_e():
    try:
        global e
        e = float(input_prompt.text())
        input_prompt.clear()
    except:
        pass

def get_f():
    try:
        global f
        f = float(input_prompt.text())
        input_prompt.clear()
    except:
        pass

def solvef():
    try:
        global total
        D = a*e-b*d
        Dx = c*e-b*f
        Dy = a*f-d*c
        x = Dx/D
        y = Dy/D
        total += "\nx=" + str(x) + "\ny=" + str(y) + "\n"
        display.setText(total)
    except:
        total = welcome
        display.setText(total)

app = QApplication([])
w = QWidget()
w.setWindowTitle("system solver")
w.resize(700, 500)
display = QTextEdit()
display.setReadOnly(True)
input_prompt = QLineEdit()
input_prompt.setPlaceholderText('Type here:')
pb1 = QPushButton("a")
pb2 = QPushButton("b")
pb3 = QPushButton("c")
pb4 = QPushButton("d")
pb5 = QPushButton("e")
pb6 = QPushButton("f")
pb7 = QPushButton("Find")
lv1 = QVBoxLayout()
lh1 = QHBoxLayout()
lh2 = QHBoxLayout()
lh3 = QHBoxLayout()
lv1.addWidget(input_prompt)
lh1.addWidget(pb1)
lh1.addWidget(pb2)
lh1.addWidget(pb3)
lh2.addWidget(pb4)
lh2.addWidget(pb5)
lh2.addWidget(pb6)
lv1.addLayout(lh1)
lv1.addLayout(lh2)
lv1.addWidget(pb7)
lh3.addWidget(display)
lh3.addLayout(lv1)
w.setLayout(lh3)
w.show()
total = ''
welcome = 'The program displays the values of the x and y provided they exist\nthe form of the system is:\na*x + b*y = c\nd*x + e*y = f\n'
total += welcome
display.setText(total)
pb1.clicked.connect(get_a)
pb2.clicked.connect(get_b)
pb3.clicked.connect(get_c)
pb4.clicked.connect(get_d)
pb5.clicked.connect(get_e)
pb6.clicked.connect(get_f)
pb7.clicked.connect(solvef)
app.exec()