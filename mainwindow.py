from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from Libreria01.libreria import Libreria
from Libreria01.libro import Libro
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.libreria = Libreria()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Agregar_Final_pushButton.clicked.connect(self.click_agregar)
        self.ui.Agregar_Inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.Mostrar_pushbutton.clicked.connect(self.click_mostrar)
    @Slot()
    def click_mostrar(self):
        #self.libreria.mostrar()
        self.ui.Salida.clear()
        self.ui.Salida.insertPlainText(str(self.libreria))
    
    @Slot()
    def click_agregar(self):
        titulo = self.ui.Titulo_lineEdit_2.text()
        autor = self.ui.Autor_lineEdit.text()
        publicado = self.ui.Publicado_spinbox.value()
        editorial = self.ui.Editorial_lineEdit.text()

        libro = Libro(titulo, autor, publicado, editorial)
        self.libreria.agregar_final(libro)
    @Slot()
    def click_agregar_inicio(self):
        titulo = self.ui.Titulo_lineEdit_2.text()
        autor = self.ui.Autor_lineEdit.text()
        publicado = self.ui.Publicado_spinbox.value()
        editorial = self.ui.Editorial_lineEdit.text()

        libro = Libro(titulo, autor, publicado, editorial)
        self.libreria.agregar_final(libro)