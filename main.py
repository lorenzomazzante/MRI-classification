import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap, QPalette, QColor
from PyQt6.QtCore import Qt

class InitialWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App for detecting tumors")

        # Configurar fondo oscuro
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(Qt.GlobalColor.gray))
        self.setPalette(palette)

        # Fijar tamaño de la ventana inicial
        self.setFixedSize(1000, 600)  # Cambia estos valores según lo necesites

        # Crear botón "Iniciar aplicación"
        self.init_button = QPushButton("Start app", self)
        self.init_button.clicked.connect(self.start_application)
        self.init_button.setGeometry(400, 275, 200, 50)

    def start_application(self):
        # Ocultar la ventana inicial y mostrar la ventana principal
        self.hide()
        self.main_window = MainWindow()
        self.main_window.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App for detecting tumors")

        # Configurar fondo oscuro
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(Qt.GlobalColor.gray))
        self.setPalette(palette)

        # Fijar tamaño de la ventana principal
        self.setFixedSize(1000, 600)  # Cambia estos valores según lo necesites

        # Crear un widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Crear el layout
        layout = QVBoxLayout(self.central_widget)

     # Mostrar texto "MRI to analyze"
        self.label = QLabel("MRI TO ANALYZE", self.central_widget)
        self.label.setGeometry(140, 30, 200, 30)  # Ajusta posición y tamaño del QLabel
        self.label.setStyleSheet("font-size: 15px;")  # Ajustar el tamaño de la fuente

        # Cargar y mostrar la imagen
        self.image_label = QLabel(self.central_widget)
        pixmap = QPixmap("C:/Users/Mariano/Documents/Lorenzo/Boludines/MRI - clasification/aplication/image_to_analyze.jpg")
        pixmap = pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio)  # Escalar la imagen
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(30, 70, 400, 400)  # Ajustar posición y tamaño del QLabel
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Crear botón "Start Prediction"
        self.start_button = QPushButton("Start Prediction", self.central_widget)
        self.start_button.setGeometry(20, 530, 960, 50)  # Ajusta posición y tamaño del botón
        self.start_button.clicked.connect(self.start_prediction)

    def start_prediction(self):
        print("Iniciando predicción...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Mostrar la ventana inicial
    initial_window = InitialWindow()
    initial_window.show()
    
    sys.exit(app.exec())