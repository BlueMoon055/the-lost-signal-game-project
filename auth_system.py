"""
Система аутентификации для игры The Lost Signal
Автоматически сохраняет данные пользователей на PC
После регистрации показывает окно входа
"""

import json
import os
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class AuthSystem:
    """Система входа и регистрации"""

    def __init__(self):
        self.users_file = "users.json"  # Файл для хранения данных
        self.game_data_file = "game_progress.json"  # Файл для прогресса
        self.current_user = None
        self.users = self.load_users()
        self.game_data = self.load_game_data()
        self.auth_callback = None  # Callback для успешного входа

    def load_users(self):
        """Загрузка пользователей из файла"""
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def load_game_data(self):
        """Загрузка данных игры"""
        if os.path.exists(self.game_data_file):
            try:
                with open(self.game_data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def save_data(self):
        """Сохранение всех данных"""
        with open(self.users_file, 'w', encoding='utf-8') as f:
            json.dump(self.users, f, ensure_ascii=False, indent=2)
        with open(self.game_data_file, 'w', encoding='utf-8') as f:
            json.dump(self.game_data, f, ensure_ascii=False, indent=2)

    def show_auth_popup(self, callback):
        """
        Показать окно входа/регистрации
        callback - функция, которая вызовется после успешной авторизации
        """
        self.auth_callback = callback

        # Создаем содержимое попапа
        content = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.reg_success_label = Label(
            text='',
            color=(0.2, 0.8, 0.2, 1),  # Зеленый цвет
            size_hint_y=None,
            height=30
        )

        # Заголовок
        title = Label(
            text='Вход в игру',
            font_size=24,
            size_hint=(1, 0.2)
        )

        # Поля ввода
        self.username_input = TextInput(
            hint_text='Имя пользователя',
            multiline=False,
            size_hint_y=None,
            height=40
        )

        self.password_input = TextInput(
            hint_text='Пароль',
            password=True,
            multiline=False,
            size_hint_y=None,
            height=40
        )

        # Кнопки
        buttons_layout = BoxLayout(spacing=10, size_hint_y=None, height=50)

        login_btn = Button(
            text='Войти',
            background_color=(0.2, 0.6, 0.8, 1)
        )
        login_btn.bind(on_press=self.try_login)

        register_btn = Button(
            text='Регистрация',
            background_color=(0.7, 0.5, 0.9, 1)  # Фиолетовый
        )
        register_btn.bind(on_press=self.show_register_popup)

        buttons_layout.add_widget(login_btn)
        buttons_layout.add_widget(register_btn)

        # Сообщение об ошибке
        self.error_label = Label(
            text='',
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=30
        )

        # Собираем всё
        content.add_widget(title)
        content.add_widget(self.reg_success_label)  # ★★★★ ДОБАВЛЕНО ★★★★
        content.add_widget(self.username_input)
        content.add_widget(self.password_input)
        content.add_widget(self.error_label)
        content.add_widget(buttons_layout)

        # Создаем попап
        self.auth_popup = Popup(
            title='Аутентификация',
            content=content,
            size_hint=(0.8, 0.6),
            auto_dismiss=False
        )

        # Открываем попап
        self.auth_popup.open()

    def try_login(self, instance):
        """Попытка входа"""
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()

        if not username or not password:
            self.error_label.text = 'Заполните все поля'
            return

        if username in self.users:
            if self.users[username] == password:
                # Успешный вход
                self.current_user = username

                # Создаем запись в игровых данных, если её нет
                if username not in self.game_data:
                    self.game_data[username] = {
                        'level': 1,
                        'score': 0,
                        'play_time': 0
                    }
                    self.save_data()

                self.error_label.color = (0.2, 0.8, 0.2, 1)  # Зеленый
                self.error_label.text = f'Успешный вход! Добро пожаловать, {username}!'

                self.auth_popup.dismiss()
                self.auth_callback(username)  # Вызываем callback
            else:
                self.error_label.text = 'Неверный пароль'
        else:
            self.error_label.text = 'Пользователь не найден'

            # После успешного входа:
            from kivy.app import App
            App.get_running_app().show_game_screen(username)

    def show_register_popup(self, instance):
        """Показать окно регистрации"""
        # Закрываем текущий попап
        self.auth_popup.dismiss()

        # Создаем содержимое для регистрации
        content = BoxLayout(orientation='vertical', spacing=10, padding=20)

        title = Label(
            text='Регистрация',
            font_size=24,
            size_hint=(1, 0.2)
        )

        self.reg_username_input = TextInput(
            hint_text='Придумайте имя пользователя',
            multiline=False,
            size_hint_y=None,
            height=40
        )

        self.reg_password_input = TextInput(
            hint_text='Придумайте пароль',
            password=True,
            multiline=False,
            size_hint_y=None,
            height=40
        )

        self.reg_confirm_input = TextInput(
            hint_text='Подтвердите пароль',
            password=True,
            multiline=False,
            size_hint_y=None,
            height=40
        )

        # Кнопки
        buttons_layout = BoxLayout(spacing=10, size_hint_y=None, height=50)

        register_btn = Button(
            text='Зарегистрироваться',
            background_color=(0.7, 0.5, 0.9, 1)  # Фиолетовый
        )
        register_btn.bind(on_press=self.try_register)

        back_btn = Button(
            text='Назад',
            background_color=(0.5, 0.5, 0.5, 1)
        )
        back_btn.bind(on_press=lambda x: (self.reg_popup.dismiss(), self.show_auth_popup(self.auth_callback)))

        buttons_layout.add_widget(register_btn)
        buttons_layout.add_widget(back_btn)

        # Сообщение об ошибке
        self.reg_error_label = Label(
            text='',
            color=(1, 0.3, 0.3, 1),
            size_hint_y=None,
            height=30
        )

        # Собираем всё
        content.add_widget(title)
        content.add_widget(self.reg_username_input)
        content.add_widget(self.reg_password_input)
        content.add_widget(self.reg_confirm_input)
        content.add_widget(self.reg_error_label)
        content.add_widget(buttons_layout)

        # Создаем попап
        self.reg_popup = Popup(
            title='Регистрация',
            content=content,
            size_hint=(0.8, 0.7),
            auto_dismiss=False
        )

        self.reg_popup.open()

    def try_register(self, instance):
        """Попытка регистрации"""
        username = self.reg_username_input.text.strip()
        password = self.reg_password_input.text.strip()
        confirm = self.reg_confirm_input.text.strip()

        # Проверки
        if not username or not password or not confirm:
            self.reg_error_label.text = 'Заполните все поля'
            return

        if len(username) < 3:
            self.reg_error_label.text = 'Имя должно быть не менее 3 символов'
            return

        if len(password) < 4:
            self.reg_error_label.text = 'Пароль должен быть не менее 4 символов'
            return

        if password != confirm:
            self.reg_error_label.text = 'Пароли не совпадают'
            return

        if username in self.users:
            self.reg_error_label.text = 'Имя пользователя уже занято'
            return

        self.users[username] = password
        self.game_data[username] = {
            'level': 1,
            'score': 0,
            'play_time': 0,
            'created_at': 'today'
        }

        # Сохраняем данные
        self.save_data()

        #Показываем сообщение об успешной регистрации
        success_popup = Popup(
            title='Успех!',
            content=Label(text=f'Аккаунт "{username}" успешно создан!\nТеперь войдите в систему.'),
            size_hint=(0.6, 0.4)
        )
        success_popup.open()

        self.reg_popup.dismiss()

        # Показываем окно входа с сообщением об успешной регистрации
        def show_auth_with_message():
            self.show_auth_popup(self.auth_callback)
            # Устанавливаем логин в поле ввода
            self.username_input.text = username
            # Показываем сообщение об успешной регистрации
            self.reg_success_label.text = f'Аккаунт "{username}" успешно создан!'

        # Небольшая задержка для красоты
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: show_auth_with_message(), 0.5)

    def get_user_data(self, username=None):
        """Получить данные пользователя"""
        if username is None:
            username = self.current_user

        if username in self.game_data:
            return self.game_data[username]
        return None

    def update_user_data(self, data, username=None):
        """Обновить данные пользователя"""
        if username is None:
            username = self.current_user

        if username in self.game_data:
            self.game_data[username].update(data)
            self.save_data()
            return True
        return False

    def logout(self):
        """Выход из аккаунта"""
        self.current_user = None