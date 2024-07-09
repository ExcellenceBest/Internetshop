Интернет магазин
1. Создаю виртуальное окружение командой python -m venv venv
2. Активация окружения командой venv\Scripts\activate.bat  
3. Установка Джанго (лучше через vscode) командой pip install django
4. Создал проект командой django-admin startproject shop . (Точка нужна чтоб не создался проект папка в папке).
5. Создаю приложение командой python manage.py startapp main
6. Запуск сервера командой python manage.py runserver
7. Создаю приложение командой python manage.py startapp basket
8. Создаю приложение командой python manage.py startapp catalog
9. Создаю приложение командой python manage.py startapp contacts
10. Зарегистрировал приложения в файле settings в проекте
11. Вынес маршруты приложений в сами приложения и подключил через include