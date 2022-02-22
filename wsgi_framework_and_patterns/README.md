# #wsgi, patterns
## Задание на проектирование:
> - Написать собственный wsgi-framework.
> - Написать на его базе приложение, описывающее обучающий сайт.
> 
> Создание категории курсов
> 
> Вывод списка категорий
> 
> Создание курса
> 
> Вывод списка курсов
> - Применить ряд паттернов.
> - Упор сделать на применение паттернов.
> - Добавить декоратор для добавления связки url-view в приложение,
> чтобы можно было добавлять url-ы, как в фреймворке Flask @app(‘/some_url/’).
> - Добавить декоратор @debug, для view, если мы указываем данный декоратор над view,
> то в терминал выводятся название функции и время ее выполнения.
> - Добавить 2 новых вида wsgi-application. Первый - логирующий
> (такой же как основной, только он для каждого запроса выводит информацию
> (тип запроса и параметры) в консоль. Второй - фейковый
> (на все запросы пользователя отвечает “200 OK”, “Hello from Fake”).
> - Реализовать простой логгер без использования сторонних библиотек.

## Реализация
1. Собственно "framework" (квадратное колесо) во вложенной папке amoeba/amoeba.
2. Шаблоны страниц в папке templates.
3. В папке patterns некоторые базовые паттерны.
4. В папке models реализация моделей с использованием паттернов.
5. Добавлно API для получения курсов в формате json.
6. Декоратор debug в models/debug.
7. Вызов двух дополнительных wsgi-applications (логирующего и фейкового)
   прописан в app.ru
8. Логгер в models/logger. Добавлен выбор "writer" для логгера.

## Запуск:
Для Unix:

*gunicorn app:app*

Для Windows:

*waitress-serve --listen=\*:8000 app:app*