Вашему вниманию представлен чат-бот для записи на сдачи.  
Бот дает студенту возможность записаться на сдачу в процессе переписки на сайе, 
преподавателям зайти на сайт и увидеть очередь сдающих.
Ниже инструкция по установке:
1. Бот работает на основе фреймворка rasa версий от 1.10.x до 2.x(не включительно).
Первое, что требуется для избежания различных конфликтов - это вручную установить подходящую версию фреймворка на сервере, 
доступность версии зависит от того, какая у Вас ОС и какая версия python3.
Рекомендуемые требования: Ubuntu 18.04 и python 3.7.9. Подробнейшая инструкция по установке:
https://legacy-docs-v1.rasa.com/user-guide/installation/
2. Помимо сервера для модели, требуется база данных postgresql, данные для входа пользователя, имя базы данных и ее url. 
Команды:
```
CREATE TABLE it (
  Name text NOT NULL,
  Number INT NOT NULL
);

CREATE TABLE math (
  Name text NOT NULL,
  Number INT NOT NULL
);

CREATE TABLE phys (
  Name text NOT NULL,
  Number INT NOT NULL
);

CREATE TABLE rasa ();
``` 
Далее, в endpoints.yml нужно отредактировать следующее:

```
tracker_store:
    type: SQL
    dialect: "postgresql" 
    url: "" # url базы данных
    db: "" # имя базы данных
    username: "" # имя пользователя
    password: "" # пароль 
```
Эти же параметры передать в файлы web/one.php, web/two.php, web/three.php в переменные $host, $db, $user и $pass. 
То же самое добавить в actions.py в класс ActionGetTable (два заметных места в коде).
3. На сервере сделать три вкладки tmux:
```
$ sudo apt-get upgrade
$ sudo apt-get install tmux
$ tmux new -s actions && tmux new -s core && tmux new -s train
```
Активировать ваше виртуальное окружение и зайти в папку проекта в каждой из вкладок, после чего выполнить:  
В train: 
```
$ rasa data validate
$ rasa train --force
```
В actions: 
```
$ rasa run actions --debug
```
В core: 
```
$ rasa run -m models --enable-api --cors "*" --endpoints endpoints.yml --debug
```
4. скопировать содержимое папки web на хостинг Вашего домена.
