#!/usr/bin/python3

# sudo apt install python3-pyqt6

# Only needed for access to command line arguments
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui  import QFont, QPixmap, QPalette, QColor
#from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QLabel
from PyQt6.QtWidgets import (
   QApplication,
   QCheckBox,
   QComboBox,
   QDateEdit,
   QDateTimeEdit,
   QDial,
   QDoubleSpinBox,
   QFrame,
   QFontComboBox,
   QLabel,
   QLCDNumber,
   QLineEdit,
   QMainWindow,
   QProgressBar,
   QPushButton,
   QRadioButton,
   QSlider,
   QSpinBox,
   QTimeEdit,
   QVBoxLayout,
   QHBoxLayout,
   QGridLayout,
   QWidget,
)

DEF_T1_SZ = 300
DEF_T2_SZ = 300
DEF_TXT_SZ = 300

DEF_SM = 14

DEF_T1_NAME = 'King'
DEF_T2_NAME = 'Richi'

DEF_TXT = 'GO THUNDERDOME!'

DEF_T1_COLOR = 'red'
DEF_T2_COLOR = 'yellow'
DEF_TXT_COLOR = 'orange'

DEF_BG_COLOR = 'dark blue'

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

#
# Control Window
#
class SubWindow(QMainWindow):
    def __init__(self, mw, box):
        super().__init__()
        self.mw = mw
        self.box = box

        self.t1_name_sz = DEF_T1_SZ
        self.t2_name_sz = DEF_T2_SZ

        self.t1_score_sz = DEF_T1_SZ
        self.t2_score_sz = DEF_T2_SZ
        self.box_sz = DEF_TXT_SZ

        self.setWindowTitle("Control")

        color = 'color: white; background-color: black;'
        self.col1 = QLabel('         ')
        self.col2 = QLabel('Team Name')
        self.col2.setStyleSheet(color)
        self.col3 = QLabel('Team Score')
        self.col3.setStyleSheet(color)
        self.t1s = QLabel('T1 sz')
        self.t1s.setStyleSheet(color)
        self.t2s = QLabel('T2 sz')
        self.t2s.setStyleSheet(color)
        self.box_s = QLabel('BOX sz')
        self.box_s.setStyleSheet(color)

        self.t1 = QLabel('TEAM 1')
        self.t1.setStyleSheet(color)
        self.t1_input_name = QLineEdit(DEF_T1_NAME)
        self.t1_input_name.textChanged.connect(self.mw.t1_name.setText)
        t1_f = self.t1_input_name.font()
        t1_f.setPointSize(DEF_SM)
        self.t1_input_name.setFont(t1_f)

        self.t1_input_score = QLineEdit('0')
        self.t1_input_score.textChanged.connect(self.mw.t1_score.setText)
        t1_f = self.t1_input_score.font()
        t1_f.setPointSize(DEF_SM)
        self.t1_input_score.setFont(t1_f)

        self.t1_name_size = QLineEdit(str(DEF_T1_SZ))
        self.t1_name_size.textChanged.connect(self.t1_name_size_changed)
        f_f = self.t1_name_size.font()
        f_f.setPointSize(DEF_SM)
        self.t1_name_size.setFont(f_f)

        self.t1_score_size = QLineEdit(str(DEF_T1_SZ))
        self.t1_score_size.textChanged.connect(self.t1_score_size_changed)
        f_f = self.t1_score_size.font()
        f_f.setPointSize(DEF_SM)
        self.t1_score_size.setFont(f_f)


        self.t2 = QLabel('TEAM 2')
        self.t2.setStyleSheet(color)
        self.t2_input_name = QLineEdit(DEF_T2_NAME)
        self.t2_input_name.textChanged.connect(self.mw.t2_name.setText)
        t2_f = self.t2_input_name.font()
        t2_f.setPointSize(DEF_SM)
        self.t2_input_name.setFont(t2_f)

        self.t2_input_score = QLineEdit('0')
        self.t2_input_score.textChanged.connect(self.mw.t2_score.setText)
        t2_f = self.t2_input_score.font()
        t2_f.setPointSize(DEF_SM)
        self.t2_input_score.setFont(t2_f)

        self.t2_name_size = QLineEdit(str(DEF_T2_SZ))
        self.t2_name_size.textChanged.connect(self.t2_name_size_changed)
        f_f = self.t2_name_size.font()
        f_f.setPointSize(DEF_SM)
        self.t2_name_size.setFont(f_f)

        self.t2_score_size = QLineEdit(str(DEF_T2_SZ))
        self.t2_score_size.textChanged.connect(self.t2_score_size_changed)
        f_f = self.t2_score_size.font()
        f_f.setPointSize(DEF_SM)
        self.t2_score_size.setFont(f_f)

        self.box_size = QLineEdit(str(DEF_TXT_SZ))
        self.box_size.textChanged.connect(self.box_size_changed)
        f_f = self.box_size.font()
        f_f.setPointSize(DEF_SM)
        self.box_size.setFont(f_f)

        self.t1_button = QPushButton('SET SIZE')
        color = 'color: white; background-color: green;'
        self.t1_button.setStyleSheet(color)
        self.t1_button.clicked.connect(self.t1_clicked)

        color = 'color: white; background-color: black;'
        self.boxl = QLabel('BOX TXT')
        self.boxl.setStyleSheet(color)

        self.txt_input = QLineEdit(DEF_TXT)
        self.txt_input.textChanged.connect(self.box.text.setText)
        txt_f = self.txt_input.font()
        txt_f.setPointSize(DEF_SM)
        self.txt_input.setFont(txt_f)

        self.quit_button = QPushButton('EXIT')
        color = 'color: white; background-color: red;'
        self.quit_button.setStyleSheet(color)
        self.quit_button.clicked.connect(self.quit)
        
        # line separator
        self.line = QFrame()
        #self.line.setFrameShape(QFrame.HLine)
        #self.line.setFrameShadow(QFrame.Sunken)
        self.line.setStyleSheet('color: dark blue;')
        l_sep = QHBoxLayout()
        l_sep.addWidget(self.line)

        l_ov = QVBoxLayout()
        # team names & scores
        t_l = QVBoxLayout()
        l_1 = QHBoxLayout()
        l_2 = QHBoxLayout()
        l_3 = QHBoxLayout()

        # sizes, button
        s_l = QVBoxLayout()
        l_4 = QHBoxLayout()
        l_5 = QHBoxLayout()
        l_6 = QHBoxLayout()
        l_7 = QHBoxLayout()

        # box window
        b_l = QVBoxLayout()
        l_8 = QHBoxLayout()

        # exit
        e_l = QVBoxLayout()
        l_9 = QHBoxLayout()

        l_1.addWidget(self.col1)
        l_1.addWidget(self.col2)
        l_1.addWidget(self.col3)

        l_2.addWidget(self.t1)
        l_2.addWidget(self.t1_input_name)
        l_2.addWidget(self.t1_input_score)

        l_3.addWidget(self.t2)
        l_3.addWidget(self.t2_input_name)
        l_3.addWidget(self.t2_input_score)

        t_l.addLayout(l_1)
        t_l.addLayout(l_2)
        t_l.addLayout(l_3)
        t_l.addLayout(l_sep)

        l_4.addWidget(self.t1s)
        l_4.addWidget(self.t1_name_size)
        l_4.addWidget(self.t1_score_size)

        l_5.addWidget(self.t2s)
        l_5.addWidget(self.t2_name_size)
        l_5.addWidget(self.t2_score_size)
        l_6.addWidget(self.box_s)
        l_6.addWidget(self.box_size)
        l_7.addWidget(self.t1_button)

        s_l.addLayout(l_4)
        s_l.addLayout(l_5)
        s_l.addLayout(l_6)
        s_l.addLayout(l_7)
        s_l.addLayout(l_sep)

        l_8.addWidget(self.boxl)
        l_8.addWidget(self.txt_input)
        b_l.addLayout(l_8)
        b_l.addLayout(l_sep)

        l_9.addWidget(self.quit_button)
        e_l.addLayout(l_9)

        l_ov.addLayout(t_l)
        l_ov.addLayout(s_l)
        l_ov.addLayout(b_l)
        l_ov.addLayout(e_l)

        container = Color('black')
        container.setLayout(l_ov)
        self.setCentralWidget(container)

    def t1_clicked(self):
        fonzn = QFont("Helvetica", self.t1_name_sz)
        fonzn.setBold(True)
        self.mw.t1_name.setFont(fonzn)
        fonzs = QFont("Helvetica", self.t1_score_sz)
        fonzs.setBold(True)
        self.mw.t1_score.setFont(fonzs)

        fonzn = QFont("Helvetica", self.t2_name_sz)
        fonzn.setBold(True)
        self.mw.t2_name.setFont(fonzn)
        fonzs = QFont("Helvetica", self.t2_score_sz)
        fonzs.setBold(True)
        self.mw.t2_score.setFont(fonzs)

        fonzb = QFont("Helvetica", self.box_sz)
        fonzb.setBold(True)
        self.box.text.setFont(fonzb)

    def quit(self):
        sys.exit(0)

    def t1_name_size_changed(self, newsize):
        try:
            self.t1_name_sz = int(newsize)
        except:
            pass

    def t1_score_size_changed(self, newsize):
        try:
            self.t1_score_sz = int(newsize)
        except:
            pass

    def t2_name_size_changed(self, newsize):
        try:
            self.t2_name_sz = int(newsize)
        except:
            pass

    def t2_score_size_changed(self, newsize):
        try:
            self.t2_score_sz = int(newsize)
        except:
            pass

    def box_size_changed(self, newsize):
        try:
            self.box_sz = int(newsize)
        except:
            pass


#
# ONE BOX Window
#
class OneBoxWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(DEF_BG_COLOR))
        self.setPalette(palette)

        self.setWindowTitle("N911!")
        #button = QPushButton("Press Me!")
        #self.setFixedSize(QSize(400,300))

        fonz_txt = QFont("Helvetica", DEF_TXT_SZ)
        fonz_txt.setBold(True)

        self.text = QLabel(DEF_TXT)
        self.text.setFont(fonz_txt)
        self.text.setWordWrap(True)
        self.text.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        text_color = 'color: %s; background-color: black;  border: white;' % (DEF_TXT_COLOR)
        self.text.setStyleSheet(text_color)

        l_ov = QHBoxLayout()
        l_ov.addWidget(self.text)
        container = Color(DEF_BG_COLOR)
        container.setLayout(l_ov)
        # Set the central widget of the Window.
        self.setCentralWidget(container)

#
# Display Window
#
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(DEF_BG_COLOR))
        self.setPalette(palette)

        self.setWindowTitle("N911 Scoreboard!")

        self.t1_name = QLabel(DEF_T1_NAME)
        self.t1_score = QLabel('0')

        self.t2_name = QLabel(DEF_T2_NAME)
        self.t2_score = QLabel('0')

        fonz_t1 = QFont("Helvetica", DEF_T1_SZ)
        fonz_t1.setBold(True)
        fonz_t2 = QFont("Helvetica", DEF_T2_SZ)
        fonz_t2.setBold(True)

        self.t1_name.setFont(fonz_t1)
        self.t1_name.setWordWrap(True)
        self.t1_name.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        t1_col_n = 'color: %s; background-color: black;  border: white;' % (DEF_T1_COLOR)
        t1_col_s = 'color: black; background-color: %s;  border: white;' % (DEF_T1_COLOR)
        self.t1_name.setStyleSheet(t1_col_n)

        self.t1_score.setFont(fonz_t1)
        self.t1_score.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.t1_score.setStyleSheet(t1_col_s)

        self.t2_name.setFont(fonz_t2)
        self.t2_name.setWordWrap(True)
        self.t2_name.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        t2_col_n = 'color: %s; background-color: black;  border: white;' % (DEF_T2_COLOR)
        t2_col_s = 'color: black; background-color: %s;  border: white;' % (DEF_T2_COLOR)
        self.t2_name.setStyleSheet(t2_col_n)

        self.t2_score.setFont(fonz_t2)
        self.t2_score.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.t2_score.setStyleSheet(t2_col_s)

        #self.pic = QLabel()
        #self.pic.setPixmap(QPixmap('madmax.png'))
        #self.pic.setMaximumSize(500,300)
        #self.pic.setScaledContents(True)

        #layout = QVBoxLayout()    # QVBoxLayout, QGridLayout, QStackedLayout
        l_ov = QHBoxLayout()
        l_na = QVBoxLayout()
        l_sc = QVBoxLayout()

        l_na.addWidget(self.t1_name)
        l_na.addWidget(self.t2_name)

        l_sc.addWidget(self.t1_score)
        l_sc.addWidget(self.t2_score)

        l_ov.addLayout(l_na)
        l_ov.addLayout(l_sc)

        #layout.addWidget(self.pic)

        widgets = [
             QCheckBox,
             QComboBox,
             QDateEdit,
             QDateTimeEdit,
             QDial,
             QDoubleSpinBox,
             QFontComboBox,
             QLCDNumber,
             QLabel,
             QLineEdit,
             QProgressBar,
             QPushButton,
             QRadioButton,
             QSlider,
             QSpinBox,
             QTimeEdit,
        ]

        #for w in widgets:
        #    layout.addWidget(w())
        
        #container = QWidget()
        container = Color(DEF_BG_COLOR)
        container.setLayout(l_ov)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

app = QApplication(sys.argv)

scoreboard = MainWindow()
scoreboard.show()

onebox = OneBoxWindow()
onebox.show()

controlboard = SubWindow(scoreboard, onebox)
controlboard.show()

app.exec()
