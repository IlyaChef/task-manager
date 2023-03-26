# Task Manager

Task Manager - простой менеджер задач для командной строки. Он позволяет создавать, просматривать и перемещать таски между статусами "новый" ("new"), "в процессе" ("in progress") и "сделано" ("done"), а также задавать сроки исполнения ("deadline") для задач.

##Установка и настройка

Для установки и настройки таск-менеджера необходимо выполнить следующие шаги:

1. Установите Python 3.x, если еще не установлен
2. Склонируйте проект из репозитория на Github: https://github.com/username/task-manager
3. Установите необходимые библиотеки с помощью команды: <font color="#grey">pip install -r requirements.txt</font> 
4. Создайте базу данных с помощью команды: <font color="#grey">alembic upgrade head</font>
5. Таск-менеджер готов к запуску.

## Использование

Для запуска таск-менеджера необходимо запустить main.py из консоли, дописав нужную команду:

- <font color="#grey">create</font> - создать новый таск
- <font color="#grey">show</font>  - показать все новые таски (todo-лист задач)
- <font color="#grey">move</font>  - переместить таск из нового в другой статус ("in_progress", "done")
- <font color="#grey">doing</font>  - показать таски, которые находятся в процессе выполнения (в статусе "in_progress")
- <font color="#grey">deadline</font> - показать список задач со сроком исполнения до указанной вами даты

Для получения справки по каждой команде можно использовать опцию <font color="#grey">-h</font>, <font color="#grey">--help</font> 

### Создание нового таска
Для того, чтоб создать новый таск, надо при запуске скрипта выполнить команду create, сообщив в строку значения аргументов <font color="#grey">--title</font>, <font color="#grey">--description</font> и <font color="#grey">--deadline</font>. Пример:

    python main.py create --title "Тесты" --description "Написать тесты на функции" --deadline "2023-03-28"

### Просмотр перечня новых тасков:

    python main.py show

Появится todo-лист ваших задач со статусом "new". Пример:

    1. Первый таск - status: new (deadline: 2023-03-28)  *** description: Сдать этот код на ревью
    2. Тесты - status: new (deadline: 2023-03-27)  *** description: Накатать тестов
    3. CI - status: new (deadline: 2023-03-27)  *** description: Накатать review.yml для GA
    4. flake8 - status: new (deadline: 2023-03-26)  *** description: Сконфигурировать flake8 и все проверить
    5. MyPy - status: new (deadline: 2023-03-26)  *** description: Сконфигурировать MyPy и все проверить
    6. Alembic - status: new (deadline: 2023-03-26)  *** description: Накатать Alembic
    7. README.md - status: new (deadline: 2023-03-28)  *** description: Написать, как пользоваться скриптом

Выбрав задачу на выполнение, переместите ее в статус <font color="#grey">'in_progress'</font>, сообщив в строку ее номер:

    python main.py move 1 in_progress

### Просмотр списка задач в процессе выполнения:

    python main.py doing


### Просмотр списка задач с дэдлайном до указанной вами даты:

    python main.py deadline YYYY-MM-DD

Пример:

    >> python main.py deadline 2023-03-27 
    4. flake8 - status: new (deadline: 2023-03-26)  *** description: Сконфигурировать flake8 и все проверить
    5. MyPy - status: new (deadline: 2023-03-26)  *** description: Сконфигурировать MyPy и все проверить
    6. Alembic - status: new (deadline: 2023-03-26)  *** description: Накатать Alembic
