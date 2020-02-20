import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherarquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimencionar.clicked.connect(self.redimencionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            r'/home/ricky/Imagens/'
            #options=QFileDialog.DontUseNativeDialog
        )
        self.inputAbrirarquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimencionar(self):
        largura = int(self.inputLargura.text())
        self.new_image = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap(self.new_image)
        self.inputLargura.setText(str(self.new_image.width()))
        self.inputAltura.setText(str(self.new_image.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            r'/Desktop/'
            #options=QFileDialog.DontUseNativeDialog
        )
        self.new_image.save(imagem, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
