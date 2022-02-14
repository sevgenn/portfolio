### Требования к курсовому проекту:
1) Составить общее текстовое описание БД и решаемых ею задач.
2) Минимальное количество таблиц - 10.
3) Скрипты создания структуры БД (с первичными ключами, индексами, внешними ключами).
4) Создать ERDiagram для БД.
5) Скрипты наполнения БД данными.
6) Скрипты характерных выборок (включающие группировки, JOIN'ы, вложенные таблицы).
7) Представления (минимум 2).
8) Хранимые процедуры / триггеры.
***
Чтобы не высасывать тему из пальца взял за основу то, с чем хорошо знаком из личного опыта.
Много лет занимался мебельным производством, поэтому решил написать базу данных для приложения,
которое позволяет систематизировать и администрировать процессы предприятия:
формирование заказов, отслеживание закупок, остатков, движений, статистика и анализ заказов, продаж и т.д.
Идея подойдет как для торговой фирмы, не имеющей своих производственных мощностей, так и для
производственного предприятия (в этом случае таблица "vendors" - "поставщики" будет ассоциироваться
с собственным цехом).

Рассматривалось дава варианта реализации  таблицы "товар".
В конечном варианте (2-ой вариант) товары были сведены в одну таблицу, чтобы не осложнять проверку.
Разбиение категорий товара осуществляется через дополнительную таблицу "classes" для идентификации
категорий товара (корпуса, фасады, фурнитура).

Имеющиеся таблицы и их взаимосвязь наглядно представлены на ER-diagram.

## Итого:
* Файл со скриптами создания БД 'project.sql'.

* Файл со скриптами наполнения БД 'project-insert.sql'.

* Один триггер 'date_delivery' в файле 'project.sql' формирует предварительное времени исполнения заказа
с отсрочкой 1 месяц с даты оформления заказа.

* Три представления в 'project-preview.sql'.

* Три процедуры (с входными парамеирами и без) в листе 'project-procedures.sql'.