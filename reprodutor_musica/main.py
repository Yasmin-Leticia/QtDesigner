import sys 
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

from reprodutor_musica import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.player = QMediaPlayer(self)
        self.isPaused = False
        
        self.ui.pushButton_parar.clicked.connect(self.tocar_musica)
        self.ui.pushButton_play.clicked.connect(self.tocar_musica)  
        self.ui.pushButton_pausar.clicked.connect(self.tocar_musica)    
        
    def tocar_musica(self):
        caminho_musica = os.path.abspath("musica/toque.mp3")
        print("Local da musica", caminho_musica)
        
        if self.isPaused:
            self.player.play()
            self.isPaused = False
            
        else:
            url = QUrl.fromLocalFile(caminho_musica)
        
            if url.isValid():
                self.player.setMedia(QMediaContent(url))
                self.player.play()
                print("Tocando musica...")   
                
            else:        
                print("Erro: caminho do arquivo invalido...")
            
    def parar_musica(self):
        self.player.stop()
        self.isPaused = False
        print("Música parou")
        
    def pausar_musica(self):
        self.player.pause()
        self.isPaused = True
        print("Música pausou")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
    