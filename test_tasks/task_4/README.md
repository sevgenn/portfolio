# #Django, PostgreSQL
## Задание № 4
> 1. Написать с использованием Django сайт кулинарных рецептов.
> 2. Для хранения данных использовать PostgreSql.
> 3. Реализовать возможность выбора рецептов по ингредиентам.
> 4. Реализовать возможность получения ингредиентов для конкретного рецепта.


# Сайт кулинарных рецептов

Сайт написан с использованием Django

## Запуск проекта

#### Создать базу данных Postgresql
psql -U postgres

CREATE DATABASE cookbook;

CREATE USER admin with NOSUPERUSER PASSWORD 'admin';

GRANT ALL PRIVILEGES ON DATABASE cookbook TO admin;

\q

----------------------

В виртуальной среде окружения развернуть проект.
В папке cookbook_root выполнить:
#### Установка пакетов
*pip install -r requirements.txt*
#### Применение миграций
*python manage.py migrate*
#### Добавление данных в базу
*python manage.py loaddata data_db.json*
#### Запуск сервера на http://127.0.0.1:8000
*python manage.py runserver*


(В базе уже предустановлен администратор:
admin: пароль admin
и пользователь с ограниченными правами:
user1: пароль 4esz5rdx)
