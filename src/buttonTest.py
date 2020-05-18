import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class DragDropQLE(QLineEdit):

    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [str(u.toLocalFile()) for u in event.mimeData().urls()]
        for f in files:
            fileName = f.split(".")
            fileNameExtension =fileName[len(fileName)-1]
            print("dragndropText : " +f)
            if(fileNameExtension == "zip") :
                self.setText(f)
                self.setStyleSheet(    "color : white;"
                                       "background-color : white;"
                                       "background-image : url(../rcs/icon_zip.png);"
                                       "background-repeat: no-repeat;"
                                       "border:none;")
            elif(fileNameExtension=="xlsx") :
                self.setText(f)
                self.setStyleSheet(    "color : white;"
                                       "background-color : white;"
                                       "background-image : url(../rcs/icon_xlsx.png);"
                                       "background-repeat: no-repeat;"
                                       "border:none;")
            else:
                print("올바른 파일형식을 입력해주세요")



app = QApplication(sys.argv)

#상단 상태줄 구현부

w = QWidget()

    ###실행창 크기 설정 ( 실행시 창위치, 실행시 창위치, 가로, 세로)
w.setGeometry(100,100,400,600)

    ###실행창 크기 변경 무시
w.setMinimumSize(400,600)
w.setMaximumSize(400,600)


w.setStyleSheet('background-image: url(../rcs/background_pwc_white.png)')
app.setWindowIcon(QIcon("../rcs/icon_connect.png"))


    ###실행창 명
w.setWindowTitle('ButtonTest')


# 내부 레이아웃

btn1 = QPushButton('btn1',w)
#btn1.resize(80,80)
btn1.setToolTip("this is btn1")
btn2 = QPushButton('Button2',w)

##안에 드래그앤드롭 모양
w.zip_input_qle = DragDropQLE(w)
print(w.zip_input_qle.size())
w.zip_input_qle.setFixedSize(150,150)
print(w.zip_input_qle.size())
w.zip_input_qle.setAcceptDrops(True)
w.zip_input_qle.setDragEnabled(True)
w.zip_input_qle.setEchoMode(1)
w.zip_input_qle.setStyleSheet(
    "color : black;"
    "background-color : white;"
    "border-style:dashed;"
    "border-width:1.5px;"
    "border-color:#be1f19")


w.xlsx_input_qle = DragDropQLE(w)
w.xlsx_input_qle.setAcceptDrops(True)
w.xlsx_input_qle.setDragEnabled(True)
w.xlsx_input_qle.setFixedSize(150,150)
w.xlsx_input_qle.setEchoMode(1)
w.xlsx_input_qle.setStyleSheet(
    "color : black;"
    "background-color : white;"
    "border-style:dashed;"
    "border-width:1.5px;"
    "border-color:#be1f19")


#btn3 = QPushButton('Button3',w)
#btn4 = QPushButton('Button4',w)

fileIOLayout = QHBoxLayout()
fileIOLayout.addWidget(w.xlsx_input_qle)
fileIOLayout.addWidget(w.zip_input_qle)


layout = QHBoxLayout()
layout.addWidget(btn1, 0)
layout.addWidget(btn2, 0)
#layout.addWidget(btn3, 1,1)
#layout.addWidget(btn4, 0,1)


##button에 icon이미지 입히기
btn3 = QPushButton("",w)
btn3.setIcon(QIcon("../rcs/icon_howTo.png"))
btn3.setStyleSheet("border : white")
btn3.setToolTip("도움말을 확인하고 싶으시다면, 클릭하세요.")
#btn3 click event 도움말 dialog 추가
btn3.move(325,15)


qlabel = QLabel(w)
qlabel.setText("Connect 파일 변환 프로그램")
qlabel.setStyleSheet("font-size:20px; font-family:맑은 고딕;font-weight:bold")
qlabel.adjustSize()
qlabel.move(50,100)

gridBox = QGridLayout()
#(left, top, right, bottom)
gridBox.setContentsMargins(30,200,25,150)
gridBox.addLayout(fileIOLayout,2,0)
gridBox.setSpacing(30)
gridBox.addLayout(layout,3,0)
#gridBox.addWidget(btn3)


w.setLayout(gridBox)

#btn1.resize()
#btn1.move(100,100)

#palette = QPalette()
#palette.setBrush(QPalette.Background, QBrush(QPixmap("../rcs/pwcLogo")))
#img1 = QPushButton('image',w)
#img1.setWindowIcon(QIcon('./rcs/icon_mail.png'))




w.show()

sys.exit(app.exec_())