from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
import sys

def main():
    App = QApplication(sys.argv)

    #instanciamos la main Window

    mainWindow = QMainWindow()
    mainWindow.setMinimumSize(1100,600)
    mainWindow.setMaximumSize(1100,600)

    mainWindow.show()
    App.exec()


if __name__ == "__main__":
    main()