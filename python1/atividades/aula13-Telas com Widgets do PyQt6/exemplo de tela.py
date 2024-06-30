# import sys
# from PyQt6.QtQuickWidgets import *
# #no terminal = pip install PyQt6
# app= QApplication(sys.argv)
# janela= QWidget()
# janela.resize(400,400) #primeiro o x depois o y
# janela.show()
# app.exec()



import sys
from PyQt6.QtWidgets import *

def aper():
    print("feito")
    # label.setText("senai")
    texto=line.text()  #pega o texto digitado pelo usuario
    label.setText(texto) #troca o texto
app = QApplication(sys.argv)

# with open('estilo.css','r') as file:   #r = read / estilo.css = o caminho do comando
#     app.setStyleSheet(file.read())
    
janela = QWidget()
janela.resize(400,400) # (x, y)
label=QLabel("texto de alguuma coisa",janela)
buttom=QPushButton("um botao",janela)
line=QLineEdit("",janela)
line.setGeometry(10,35,380,50)

# label.resize()            

# buttom.resize(200,200)
label.setGeometry(30,100,350,200)
buttom.setGeometry(30,100,350,200)
buttom.clicked.connect(aper)
label.setStyleSheet("background-color: black;color:white;font: 14pt MS shell Dlg 2;border-style: solid;border-color:red;border-width: 2px;border-radius: 100px;font-size: 20px")
buttom.setStyleSheet("background-color: black;color:white;font: 14pt MS shell Dlg 2;border-style: solid;border-color:red;border-width: 2px;border-radius: 100px; box-shadow: 0cm;font-size: 20px")
janela.show()
label.setGeometry(10,5,380,20) #X,Y,largura e ALTURA 
app.exec()