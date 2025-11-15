## Проект по Django "Запись на тестдрайв"
### Ркуоводство пользователя.
Проект представляет собйо сайт из 3-х страниц с функцией записи на тестдрайв.
На главной странице отображаются активные записи
<img width="790" height="499" alt="image" src="https://github.com/user-attachments/assets/eef78844-e607-414f-bef7-c4801423be63" />

Страница "О компании" содержит описание деятельности компании
<img width="1487" height="685" alt="image" src="https://github.com/user-attachments/assets/86688455-571a-4896-997a-41c40fdbeb6e" />

Страница "Тестдрайв" содержит форму записи
<img width="880" height="721" alt="image" src="https://github.com/user-attachments/assets/a4ea27b6-c39b-452a-bb0e-0b8b4c6467ca" />

После заполнения формы на странице "Главная" появляется новая активная запись
<img width="824" height="626" alt="image" src="https://github.com/user-attachments/assets/1d6ad19b-f271-4707-9345-31687b4842bf" />

### Ркуоводство программиста.
> Django — это бесплатный высокоуровневый фреймворк с открытым исходным кодом для разработки веб‑приложений на языке Python.
Начало работы со средой:
---
# Создаем виртуальную среду
python -m venv .venv
# Активируем её
.venv\Scripts\\activate
# Устанавливаем django
python -m  pip install Django==5
# Создаем проект testdrive
django-admin startproject testdrive
# Переходим в этот проект
cd testdrive
# Создаем приложение myapp
python manage.py startapp myapp
# Перейдем в файл settings.py и в разделе INSTALLED_APPS впишем в конце название приложения myapp
# Запускаем сервер
python manage.py runserver
