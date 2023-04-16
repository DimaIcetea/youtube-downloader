import sys
import os
from pytube import YouTube
import PyQt5
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QStyleFactory
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets, uic

class MyFunc(QMainWindow):
    # Устанавливаем всё нужное для класса
    def __init__(self):
        super().__init__()

        # графический интерфейс
        uic.loadUi('444.ui', self)

        # Размер окна
        self.setFixedSize(400, 600)

        # Название приложения
        self.setWindowTitle("Youtube Downloader")

        # Обработчик кликов
        self.btn_download.clicked.connect(self.btn_download_connect)
        self.btn_file.clicked.connect(self.btn_file_clicked) 
        self.info.triggered.connect(self.info_menu)
        self.add_folder.triggered.connect(self.where_input)
        self.exit_prog.triggered.connect(self.exit_p)

        # Иконка на кнопку
        pixmap = QPixmap('select.png')
        icon = QIcon(pixmap)
        self.btn_file.setIcon(icon)

        # Иконка на приложение
        pixmap_title = QPixmap('title.png')
        icon_title = QIcon(pixmap_title)
        self.setWindowIcon(icon_title)

        


    # Загрузка видео с ютуба
    def btn_download_connect(self):
            msgBox = QMessageBox()
            msgBox.setText("Загрузка началась. Ожидайте.")
            msgBox.setStandardButtons(QMessageBox.Yes)
            msgBox.setDefaultButton(QMessageBox.Yes)
            response = msgBox.exec_()
            video = YouTube(self.textEdit_file_2.toPlainText())
            video.streams.filter(progressive=True, file_extension='mp4').first().download(output_path=directory)

    # Выбрать папку для сохранения видео
    def btn_file_clicked(self):
        global directory
        directory = QFileDialog.getExistingDirectory(self, 'Выбрать директорию')
        if directory:
            self.textEdit_file.setText(directory)

    # Обработчик нажатия на меню
    def info_menu(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Информация')
        msgBox.setText("Вставьте ссылку в первое поле для ввода, затем нажмите кнопку возле второго поля для ввода. После выполнения всех действий нажмите кнопку 'Скачать' и ожидайте загрузку видео в указанную Вами папку.")
        msgBox.setStandardButtons(QMessageBox.Yes)
        msgBox.setDefaultButton(QMessageBox.Yes)
        response = msgBox.exec_()
    
    # Обработчик нажатия на меню
    def where_input(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('Помощь')
        msgBox.setText("Чтобы выбрать папку, чтобы сохранить файл, нажмите на кнопку возле второго поля ввода текста(кнопка с иконкой)")
        msgBox.setStandardButtons(QMessageBox.Yes)
        msgBox.setDefaultButton(QMessageBox.Yes)
        response = msgBox.exec_()

    # Обработчик нажатия на меню
    def exit_p(self):
         QApplication.quit()


# Обязательная составляющая программы
if __name__ == '__main__':
    app =  QApplication(sys.argv)
    window = MyFunc()
    window.show()
    QtCore.QTimer.singleShot(0, app.exec_)
    sys.exit(app.exec_())