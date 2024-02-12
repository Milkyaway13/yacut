# Укоротитель ссылок YaCut

## Описание
Проект YaCut — это сервис укорачивания ссылок. С помощью генератора можно получить вариант короткой ссылки, а также создать свою собственную версию короткой ссылки.

## Технологии
- Python 3.9
- Flask 2.0.2
- REST API
- SQLAlchemy
- HTML

## Работа с проектом

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Milkyaway13/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Cоздать файл `.env` и заполнить его слудующими данными:

    
    DATABASE_URI=<dialect+driver://username:password@host:port/database>
    FLASK_APP=yacut
    FLASK_ENV=development
    SECRET_KEY=<Ваш_секретный_ключ>
    

Создать файл базы данных и таблицы в нем:

    
    flask shell
    >>> from yacut import db
    >>> db.create_all()
    >>> exit()
    

Запустить локально:

    
    flask run


## Автор
[Боярчук Василий](https://github.com/Milkyaway13/)
