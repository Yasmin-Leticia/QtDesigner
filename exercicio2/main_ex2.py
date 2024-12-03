import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QMessageBox
from verificar_idade import Ui_MainWindow 

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setStyleSheet("""
            QMainWindow {
                background-image:('fundo.jpg');
                background-repeat: no-repeat;
                background-position: center;
            }
        """)

        self.criar_menu_bar()

        self.ui.pushButton_verificar.clicked.connect(self.verificar_idade)
    
    def criar_menu_bar(self):
        menu_bar = self.menuBar()
        
        menu_arquivo = menu_bar.addMenu("Arquivo")
        acao_sair = QAction("Sair", self)
        acao_sair.triggered.connect(self.close) 
        menu_arquivo.addAction(acao_sair)
        
        menu_ajuda = menu_bar.addMenu("Ajuda")
        acao_sobre = QAction("Sobre", self)
        acao_sobre.triggered.connect(self.mostrar_sobre)
        menu_ajuda.addAction(acao_sobre)
    
    def mostrar_sobre(self):
        QMessageBox.information(
            self,
            "Sobre o Programa",
            "Este programa verifica se uma pessoa é maior de idade (18 anos ou mais).\n\nDesenvolvido por Yasmin."
        )
    
    def verificar_idade(self):
        try:
            idade = int(self.ui.lineEdit_idade.text())

            if idade >= 18:
                mensagem = f"A pessoa tem {idade} anos e é MAIOR de idade."
            elif idade >= 0:
                mensagem = f"A pessoa tem {idade} anos e é MENOR de idade."
            else:
                mensagem = "Por favor, insira uma idade válida!" 
            
            self.ui.label_resultado.setText(mensagem)

        except ValueError:
            self.ui.label_resultado.setText("Por favor, insira uma idade válida!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainApp()
    janela.show()
    sys.exit(app.exec_())

