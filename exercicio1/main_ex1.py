import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from classificar_nota import Ui_MainWindow  # Importa a interface gerada

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Alterar a cor de fundo do QMainWindow
        self.setStyleSheet("background-color: #ffccec;")
        
        # Adicionar QLabel para exibir a imagem
        self.label_imagem = QLabel(self)
        self.label_imagem.setGeometry (650, 300, 131, 101)# Define posição e tamanho inicial
        self.label_imagem.setScaledContents(True)  # Permite que a imagem se ajuste ao QLabel
        
        # Conectar o botão à função que classifica a nota
        self.ui.pushButton_classificar.clicked.connect(self.classificar_nota)
    
    def classificar_nota(self):
        try:
            # Ler a nota do campo de entrada
            nota = float(self.ui.lineEdit_nota.text())
            
            # Inicializar classificação e caminho da imagem
            classificacao = ""
            imagem = ""
            
            # Verificar se a nota está no intervalo válido
            if 0 <= nota <= 100:
                if nota >= 90:
                    classificacao = "Excelente"
                    imagem = "excelente.png"  # Substitua pelo caminho real da sua imagem
                elif nota >= 70:
                    classificacao = "Bom"
                    imagem = "bom.png"  # Substitua pelo caminho real da sua imagem
                elif nota >= 50:
                    classificacao = "Regular"
                    imagem = "regular.png"  # Substitua pelo caminho real da sua imagem
                else:
                    classificacao = "Insuficiente"
                    imagem = "insuficiente.png"  # Substitua pelo caminho real da sua imagem
                
                
                self.ui.label_resultado.setText(f"Classificação: {classificacao}")
                
                # Atualizar a imagem no QLabel
                self.label_imagem.setPixmap(QPixmap(imagem))

            else:
                self.ui.label_resultado.setText("Por favor, insira uma nota entre 0 e 100!")
                self.label_imagem.clear()  # Limpa a imagem caso a entrada seja inválida

        except ValueError:
            self.ui.label_resultado.setText("Por favor, insira uma nota válida!")
            self.label_imagem.clear()  # Limpa a imagem caso a entrada seja inválida

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainApp()
    janela.show()
    sys.exit(app.exec_())

