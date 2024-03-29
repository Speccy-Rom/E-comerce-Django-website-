# Разработка интернет-магазина. Реализована клиентская часть сервиса и интерфейс администрирования.

#### Использовалось в проекте:
```bash
  * Frontend - Bootstrap 4
  * Backend - Django 2.2.13
  ```  
## Описание проекта.

*  В данной e-comerce решении используются 4 приложения:
```bash
  - "dshop" - раздел (функционал) самого  магазина с категориями и товарами.  
  - "cart" - корзина для покупок товара.
  - "orders" - оформление заказов, запись их в БД.
  - "accounts" - регистрация и авторизация пользователе(вход по email)
 ``` 
  
#### Документация по проекту.

Для запуска проекта необходимо:

* Установить зависимости:
```bash
pip install -r requirements.txt
```

Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py migrate
```

* Команда для запуска приложения:
```bash
python manage.py runserver
```

* При создании моделей или их изменении необходимо выполнить следующие команды:
```bash
python manage.py makemigrations
python manage.py migrate
```
* Дамп данных с тестовым наполнением:
```bash
fixtures.json
