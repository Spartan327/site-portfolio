# site-portfolio

### Проект создан для демонстраци портфолио графического дизайнера.

### На текущий момент реализовано:
- страница "об авторе";
- галерея работ;
- фильтр работ по тегу;
- просмотр работы;
- добавление работы (для администратора);
- редактирование работы (для администратора);
- авторизация зарегистрированных пользователей (регистрация доступна в административной панели Django);
- авторизация/регистрация через социальную сеть VK.

### Скриншоты:
![Image alt](screenshots/gallery.png "Страница галереи работ")
![Image alt](screenshots/about_me.png "Главная")
![Image alt](screenshots/add_paint.png "Страница добавления работы")
![Image alt](screenshots/auth.png "Страница входа")
![Image alt](screenshots/change_paint.png "Страница редактирования работы")
![Image alt](screenshots/change_paint2.png)

### Для локального развертывания необходимо:
- установить Python (https://www.python.org/downloads/);
- установить Poetry (https://python-poetry.org/docs/#installation);
- клонировать проект командой:  
`git clone https://github.com/Spartan327/site-portfolio.git`
- перейти в ветвь local-version в директории проекта и выполнить команды:
`git checkout local-version`  
`poetry install`  
`poetry run python manage.py runserver` или `poetry run python3 manage.py runserver`
- перейти по адресу http://127.0.0.1:8000/
