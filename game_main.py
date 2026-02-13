from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QListWidget
from PyQt5.QtGui import QIcon, QBrush, QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

game_layout = None

def play_clicked():
    global game_layout
    QWidget().setLayout(main_win.layout())
    palette.setBrush(main_win.backgroundRole(), QBrush(QPixmap('fon.png')))
    main_win.setPalette(palette)
    main_line2 = QVBoxLayout()
    main_line2.addWidget(story, alignment=Qt.AlignCenter)
    main_line2.addWidget(notepad, alignment=Qt.AlignCenter)
    main_line2.addWidget(gacha, alignment=Qt.AlignCenter)
    main_line2.addWidget(characters, alignment=Qt.AlignCenter)
    main_line2.addWidget(news2, alignment=Qt.AlignCenter)
    game_layout = main_line2  # сохраняем layout игры
    main_win.setLayout(main_line2)

def story_clicked():
    QWidget().setLayout(main_win.layout())
    palette.setBrush(main_win.backgroundRole(), QBrush(QPixmap('fon.png')))
    main_win.setPalette(palette)
    main_line3 = QVBoxLayout()
    h_l = QHBoxLayout()
    main_line3.addWidget(chapters, alignment=Qt.AlignCenter)
    h_l.addWidget(s1, alignment=Qt.AlignCenter)
    h_l.addWidget(ch1, alignment=Qt.AlignCenter)
    h_l.addWidget(ch2, alignment=Qt.AlignCenter)
    h_l.addWidget(ch3, alignment=Qt.AlignCenter)
    main_line3.addLayout(h_l)
    main_line3.addWidget(back, alignment=Qt.AlignCenter)
    main_win.setLayout(main_line3)

def back_clicked():
    if game_layout:  # если есть сохраненный layout игры
        QWidget().setLayout(main_win.layout())
        palette.setBrush(main_win.backgroundRole(), QBrush(QPixmap('fon.png')))
        main_win.setPalette(palette)
        main_win.setLayout(game_layout)  # возвращаемся в меню игры

app = QApplication([]) #создание объекта-приложения
app.setStyleSheet("QWidget { color: #B22222; }")  # Medium Violet Red - тёмно-розовый
# Создаем плеер
player = QMediaPlayer()
player.setMedia(QMediaContent(QUrl.fromLocalFile("музыка.mp3")))  # ваш файл
player.setVolume(50)

# Зацикливание
player.mediaStatusChanged.connect(
    lambda status: status == QMediaPlayer.EndOfMedia and player.play())

app.setWindowIcon(QIcon("icon.jpg"))
main_win = QWidget() #создание объекта-окна
main_win.resize(1588, 716) #задать размеры окна

palette = main_win.palette()
palette.setBrush(main_win.backgroundRole(), QBrush(QPixmap('fonglav.png')))
main_win.setPalette(palette)
# Установить розовый цвет для виджетов
main_win.setStyleSheet("QPushButton, QLabel { background-color: pink; }")

main_win.setWindowTitle('The Lost Signal') #задать название окну
main_win.show() #сделать объект-окно видимым


welcome = QLabel('Welcome to new world!')
welcome.setStyleSheet('font-size: 40px')
start_play = QPushButton('Play')
start_play.setFixedSize(300, 100)
start_play.setStyleSheet('font-size: 30px')
news = QPushButton('news')
news.setFixedSize(300, 100)
news.setStyleSheet('font-size: 30px')
name_game = QLabel('The Lost Signal')
name_game.setStyleSheet('font-size: 40px')
studio = QLabel('Aetherial Dream Studios')
studio.setStyleSheet('font-size: 40px')
story = QPushButton('story')
story.setFixedSize(300, 50)
story.setStyleSheet('font-size: 30px')
gacha = QPushButton('gacha')
gacha.setFixedSize(300, 50)
gacha.setStyleSheet('font-size: 30px')
characters = QPushButton('my characters')
characters.setFixedSize(300, 50)
characters.setStyleSheet('font-size: 30px')
notepad = QPushButton('notepad')
notepad.setFixedSize(300, 50)
notepad.setStyleSheet('font-size: 30px')
news2 = QPushButton('news')
news2.setFixedSize(300, 100)
news2.setStyleSheet('font-size: 30px')
chapters = QLabel('chapters:')
chapters.setStyleSheet('font-size: 60px')
ch1 = QPushButton('chapter 1')
ch1.setFixedSize(300, 100)
ch1.setStyleSheet('font-size: 30px')
ch2 = QPushButton('chapter 2')
ch2.setFixedSize(300, 100)
ch2.setStyleSheet('font-size: 30px')
ch3 = QPushButton('chapter 3')
ch3.setFixedSize(300, 100)
ch3.setStyleSheet('font-size: 30px')
s1 = QLabel('Season 1')
s1.setStyleSheet('font-size: 40px')
back = QPushButton('back')
back.setFixedSize(200, 80)
back.setStyleSheet('font-size: 30px')

main_line = QHBoxLayout() #создание горизонтальной направляющей линиии(главная)
v_line1 = QVBoxLayout() #создание вертикальной линии
v_line2 = QVBoxLayout()
v_line3 = QVBoxLayout()

v_line1.addWidget(welcome, alignment=Qt.AlignCenter)#добавление виджета на линию
v_line3.addWidget(studio, alignment=Qt.AlignCenter)
v_line3.addWidget(name_game, alignment=Qt.AlignCenter)
v_line3.addWidget(start_play, alignment=Qt.AlignCenter)
v_line3.addWidget(news, alignment=Qt.AlignCenter)

main_line.addLayout(v_line1)
main_line.addLayout(v_line2)
main_line.addLayout(v_line3)
main_win.setLayout(main_line) #загрузка заполненной линии на окно приложения

start_play.clicked.connect(play_clicked)
story.clicked.connect(story_clicked)
back.clicked.connect(back_clicked)

player.play()  # Запускаем
app.exec_() #оставлять приложение активным