from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
import json, os
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
# ★★★★ ДОБАВЬТЕ ЭТОТ ИМПОРТ ★★★★
from auth_system import AuthSystem

class MyApp(App):
    def build(self):
        Window.size = (794, 358)

        # ★★★★ ДОБАВЬТЕ ЭТОТ КОД ★★★★
        self.auth = AuthSystem()  # Создаем систему аутентификации

        layout = FloatLayout()
        bg = Image(source='фон.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(bg)

        #создаём главный горизонтальный layout
        main_layout = BoxLayout(
            orientation='horizontal')

        secondary_layout1 = BoxLayout(
            orientation='vertical')
        secondary_layout2 = BoxLayout(
            orientation='vertical')
        secondary_layout3 = BoxLayout(
            orientation='vertical')
        secondary_layout4 = BoxLayout(
            orientation='horizontal')

        # Создаем виджеты
        stu_name = Label(text='Aetherial Dream Studios')
        game_name = Label(text='The Lost Signal')
        version = Label(text='version: in progress')
        for_play = Button(
            text='Play',
            background_color=(0.8, 0.6, 0.9, 1),  #Нежно-фиолетовый
            color=(1, 1, 1, 1)  # Белый текст
        )
        # ★★★★ ДОБАВЬТЕ ЭТУ СТРОЧКУ СРАЗУ ПОСЛЕ СОЗДАНИЯ КНОПКИ ★★★★
        for_play.bind(on_press=self.on_play_clicked)

        upd_name = Label(text='Welcome to new world')

        # Добавляем виджеты в layout
        secondary_layout1.add_widget(upd_name)
        secondary_layout3.add_widget(stu_name)
        secondary_layout3.add_widget(game_name)
        secondary_layout3.add_widget(for_play)
        secondary_layout3.add_widget(version)

        main_layout.add_widget(secondary_layout1)
        main_layout.add_widget(secondary_layout2)
        main_layout.add_widget(secondary_layout3)

        #добавляем main_layout в layout с фоном
        layout.add_widget(main_layout)
        return layout

    # ★★★★ ДОБАВЬТЕ ЭТИ МЕТОДЫ В КОНЕЦ КЛАССА MyApp ★★★★

    def on_play_clicked(self, instance):
        """Обработка нажатия кнопки Play"""
        # Проверяем, авторизован ли пользователь
        if self.auth.current_user:
            # Если уже авторизован - сразу запускаем игру
            self.launch_game()
        else:
            # Если нет - показываем окно входа
            self.auth.show_auth_popup(self.launch_game)

    def launch_game(self, username=None):
        """Запуск игры после авторизации"""
        print(f"Игра запущена для пользователя: {username or self.auth.current_user}")

        # ★★★★ ЗДЕСЬ ВЫ МОЖЕТЕ ДОБАВИТЬ ПЕРЕХОД НА ИГРОВОЙ ЭКРАН ★★★★
        # Например, очистить layout и добавить игровые виджеты

if __name__ == '__main__':
    MyApp().run()