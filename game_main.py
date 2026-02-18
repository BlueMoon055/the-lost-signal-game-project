from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QStackedWidget
from PyQt5.QtGui import QIcon, QBrush, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import sys

app = QApplication(sys.argv) #создание объекта-приложения
app.setStyleSheet("QWidget { color: #B22222; }")  #тёмно-розовый
app.setWindowIcon(QIcon("icon.jpg")) #иконка приложения

# Создаем плеер
player = QMediaPlayer()
player.setMedia(QMediaContent(QUrl.fromLocalFile("музыка.mp3")))  # ваш файл
player.setVolume(50)
player.mediaStatusChanged.connect(lambda status: status == QMediaPlayer.EndOfMedia and player.play()) # Зацикливание

#окно главное
main_win = QWidget() #создание объекта-окна
main_win.resize(1588, 716) #задать размеры окна
palette = main_win.palette()
palette.setBrush(main_win.backgroundRole(), QBrush(QPixmap('fonmenu.png')))
main_win.setPalette(palette)
main_win.setStyleSheet("QPushButton, QLabel { background-color: pink; }") # Установить розовый цвет для виджетов
main_win.setWindowTitle('The Lost Signal') #задать название окну
main_win.show() #сделать объект-окно видимым

#виджеты
welcome = QLabel('Welcome, dear player!')
welcome.setStyleSheet('font-size: 40px')
news = QPushButton('news')
news.setFixedSize(300, 100)
news.setStyleSheet('font-size: 30px')
name_game = QLabel('The Lost Signal')
name_game.setStyleSheet('font-size: 40px')
studio = QLabel('Aetherial Dream Studios')
studio.setStyleSheet('font-size: 40px')
cards = QPushButton('cards')
cards.setFixedSize(300, 50)
cards.setStyleSheet('font-size: 30px')
gacha = QPushButton('gacha')
gacha.setFixedSize(300, 50)
gacha.setStyleSheet('font-size: 30px')
ch_card = QPushButton('my cards')
ch_card.setFixedSize(300, 50)
ch_card.setStyleSheet('font-size: 30px')
back = QPushButton('back')
back.setFixedSize(200, 80)
back.setStyleSheet('font-size: 30px')

main_line = QHBoxLayout() #создание горизонтальной направляющей линиии(главная)
v_line1 = QVBoxLayout() #создание вертикальной линии
v_line2 = QVBoxLayout()

v_line1.addWidget(cards, alignment=Qt.AlignCenter) #добавление виджета на линию
v_line1.addWidget(gacha, alignment=Qt.AlignCenter)
v_line1.addWidget(ch_card, alignment=Qt.AlignCenter)
v_line2.addWidget(studio, alignment=Qt.AlignCenter)
v_line2.addWidget(name_game, alignment=Qt.AlignCenter)
v_line2.addWidget(welcome, alignment=Qt.AlignCenter)
v_line2.addWidget(news, alignment=Qt.AlignCenter)

main_line.addLayout(v_line1)
main_line.addLayout(v_line2)
main_win.setLayout(main_line) #загрузка заполненной линии на окно приложения

player.play()  #Запускаем
sys.exit(app.exec_()) #оставлять приложение активным