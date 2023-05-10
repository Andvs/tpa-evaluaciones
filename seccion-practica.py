import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()


        caja_1 = QVBoxLayout()
        caja_2 = QHBoxLayout()
        caja_3 = QGridLayout()
        caja_4 = QGridLayout()

        #componenetes de la interfaz

        self.nombre = QLabel('Nombre usuario')
        self.boton_ok = QPushButton('ok')
        self.atributo1 = QLabel('Atributo')
        self.descrip_img = QLabel('Descripción imagen')
        self.img = QLabel('Img')

        #se agregan los componentes al Layout definido

        caja_1.addWidget(self.nombre)
        
        caja_1.addLayout(caja_2)
        caja_2.addLayout(caja_4)
        caja_2.addLayout(caja_3)
        
    
        caja_1.addWidget(self.boton_ok)

        caja_4.addWidget(self.img, 0,0)
        caja_4.addWidget(self.descrip_img,1,0)

        caja_3.addWidget(QLabel('Atributo 1'), 0,0)
        caja_3.addWidget(QLabel('Valor 1'), 0,1)
        caja_3.addWidget(QLabel('Atributo 2'), 1,0)
        caja_3.addWidget(QLabel('Valor 2'), 1,1)
        caja_3.addWidget(QLabel('Atributo 3'), 2,0)
        caja_3.addWidget(QLabel('Valor 3'), 2,1)
        caja_3.addWidget(QLabel('Atributo 4'), 3,0)
        caja_3.addWidget(QLabel('Valor 4'), 3,1)
        caja_3.addWidget(QLabel('Atributo 5'), 4,0)
        caja_3.addWidget(QLabel('Valor 5'), 4,1)
        caja_3.addWidget(QLabel('Atributo 6'), 5,0)
        caja_3.addWidget(QLabel('Valor 6'), 5,1)


        ventana = QWidget()
        ventana.setLayout(caja_1)
        self.setCentralWidget(ventana)
        






if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show() # obligatorio (dentro del init o fuera)
    
    #sys.close(app.exec())
    app.exec()