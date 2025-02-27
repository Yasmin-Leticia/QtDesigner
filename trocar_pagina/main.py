import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from tela_1 import Ui_MainWindow as tela_1
from tela_2 import Ui_MainWindow as tela_2

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = tela_1()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.abrir_segunda_tela)
        
    def abrir_segunda_tela(self):
        self.segunda_tela = SegundaTela()
        self.segunda_tela.show()
        self.close()
        
class SegundaTela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = tela_2()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.ui.pushButton.clicked.connect(self.voltar_para_primeira_tela)
        
    def voltar_para_primeira_tela(self):
        self.primeira_tela = Main()
        self.primeira_tela.show()
        self.close()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    sys.exit(app.exec())
        
