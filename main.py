from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from auth_system import AuthSystem

class MyApp(App):
    def build(self):
        Window.size = (794, 358)

        self.auth = AuthSystem()  # Создаем систему аутентификации

        self.main_container = FloatLayout()

        # Показываем главное меню
        self.show_main_menu()

        return self.main_container

    def show_main_menu(self):
        """Показать главное меню"""
        # Очищаем контейнер
        self.main_container.clear_widgets()

        # Фон
        bg = Image(source='фонглав.png', allow_stretch=True, keep_ratio=False)
        self.main_container.add_widget(bg)

        # Главный горизонтальный layout
        main_layout = BoxLayout(orientation='horizontal')

        secondary_layout1 = BoxLayout(orientation='vertical')
        secondary_layout2 = BoxLayout(orientation='vertical')
        secondary_layout3 = BoxLayout(orientation='vertical')

        # Создаем виджеты
        stu_name = Label(text='Aetherial Dream Studios')
        game_name = Label(text='The Lost Signal')
        version = Label(text='version: in progress')

        for_play = Button(
            text='Play',
            background_color=(1.0, 0.8, 0.9, 1),  # Нежно-розовый
            color=(1, 1, 1, 1)  # Белый текст
        )
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

        # Добавляем main_layout в контейнер
        self.main_container.add_widget(main_layout)

    def on_play_clicked(self, instance):
        """Обработка нажатия кнопки Play"""
        # Проверяем, авторизован ли пользователь
        if self.auth.current_user:
            # Если уже авторизован - сразу показываем игру
            self.show_game_screen(self.auth.current_user)
        else:
            # Если нет - показываем окно входа
            self.auth.show_auth_popup(self.show_game_screen)

    def show_game_screen(self, username=None):
        """Показать игровой экран после авторизации"""
        print(f"Игра запущена для пользователя: {username}")

        self.main_container.clear_widgets()

        # Добавляем новый фон
        bg = Image(source='фон3.png', allow_stretch=True, keep_ratio=False)
        self.main_container.add_widget(bg)

        # ★★★★ ОСНОВНОЙ КОНТЕЙНЕР ДЛЯ КНОПОК ★★★★
        buttons_container = BoxLayout(
            orientation='vertical',
            spacing=20,  # Расстояние между кнопками
            padding=50,  # Отступы от краев
            size_hint=(0.8, 0.6),  # 80% ширины, 60% высоты
            pos_hint={'center_x': 0.5, 'center_y': 0.6}  # Выше центра
        )

        # Приветствие
        welcome_label = Label(
            text=f'Добро пожаловать, {username}!',
            font_size=24,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.15),  # ★ Можно уменьшить высоту
            pos_hint={'center_x': 0.5, 'top': 0.95}  # ★★★★ СТАЛО 0.95 (выше) ★★★★
        )

        # ★★★★ КНОПКИ ИГРОВОГО МЕНЮ ★★★★
        story = Button(
            text='Story',
            size_hint=(1, 0.25),  # Занимает 25% высоты контейнера
            background_color=(1.0, 0.75, 0.8, 1),  # розовый
            color=(1, 1, 1, 1),
            font_size=20,
            bold=True
        )
        # story.bind(on_press=self.show_story_screen)  # Добавьте обработчик

        gacha = Button(
            text='Gacha',
            size_hint=(1, 0.25),  # Занимает 25% высоты контейнера
            background_color=(0.95, 0.5, 0.55, 1),  #
            color=(1, 1, 1, 1),
            font_size=20,
            bold=True
        )
        gacha.bind(on_press=self.show_gacha_screen)  # ★ ЭТА СТРОЧКА

        characters = Button(
            text='Characters',
            size_hint=(1, 0.25),  # Занимает 25% высоты контейнера
            background_color=(1.0, 0.7, 0.75, 1),  #
            color=(1, 1, 1, 1),
            font_size=20,
            bold=True
        )

        # Добавляем кнопки в контейнер
        buttons_container.add_widget(story)
        buttons_container.add_widget(gacha)
        buttons_container.add_widget(characters)

        # ★★★★ КНОПКА ВОЗВРАТА ★★★★ (НИЖЕ основного контейнера)
        back_btn = Button(
            text='Выйти в меню',
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.05},  # В самом низу
            background_color=(0.9, 0.3, 0.3, 1),
            color=(1, 1, 1, 1),
            font_size=18
        )
        back_btn.bind(on_press=lambda x: self.show_main_menu())

        # ★★★★ ДОБАВЛЯЕМ ВСЕ ВИДЖЕТЫ ★★★★
        self.main_container.add_widget(welcome_label)
        self.main_container.add_widget(buttons_container)  # Кнопки игрового меню
        self.main_container.add_widget(back_btn)  # Кнопка возврата

        #обработка нажатия на кнопку story
        story.bind(on_press=self.change_screen)  # ★ 1-я строка: привязка
        return story
    def change_screen(self, instance):
        # ★ 2-я строка: очистка экрана
        self.root.clear_widgets()
        # ★ 3-я строка: добавление нового экрана
        fon = Image(source='фон3.png', allow_stretch=True, keep_ratio=False)
        self.root.add_widget(fon)

        back_1 = Button(
            text='Назад',
            size_hint=(0.2, 0.1),
            pos_hint={'x': 0.01, 'y': 0.05},  # В самом низу
            background_color=(0.9, 0.3, 0.3, 1),
            color=(1, 1, 1, 1),
            font_size=18
        )
        back_1.bind(on_press=lambda x: self.show_game_screen())
        self.main_container.add_widget(back_1)

        story_1 = Button(
            text='chapter 1 / Цветущий сигнал',
            size_hint=(0.2, 0.1),
            pos_hint={'x': 0.71, 'y': 0.75},
            background_color=(1.0, 0.8, 0.9, 0.6),
            color=(1, 1, 1, 1),
            font_size=18
        )
        self.main_container.add_widget(story_1)

    def show_gacha_screen(self, instance):
        """Показать экран гачи"""
        self.main_container.clear_widgets()

        gacha_screen = Image(source='фон3.png', allow_stretch=True, keep_ratio=False)
        self.main_container.add_widget(gacha_screen)

        back_2 = Button(
            text='Назад',
            size_hint=(0.2, 0.1),
            pos_hint={'x': 0.01, 'y': 0.05},  # В самом низу
            background_color=(0.9, 0.3, 0.3, 1),
            color=(1, 1, 1, 1),
            font_size=18
        )
        back_2.bind(on_press=lambda x: self.show_game_screen())
        self.main_container.add_widget(back_2)

    def show_characters_screen(self, instance):
        """Показать экран characters"""
        self.main_container.clear_widgets()

        characters_screen = Image(source='фон3.png', allow_stretch=True, keep_ratio=False)
        self.main_container.add_widget(characters_screen)

        back_3 = Button(
            text='Назад',
            size_hint=(0.2, 0.1),
            pos_hint={'x': 0.01, 'y': 0.05},  # В самом низу
            background_color=(0.9, 0.3, 0.3, 1),
            color=(1, 1, 1, 1),
            font_size=18
            )
        back_3.bind(on_press=lambda x: self.show_game_screen())
        self.main_container.add_widget(back_3)



if __name__ == '__main__':
    MyApp().run()