# Консоль для управления приложениями

## Что умеем:

### Авторизация:

- /login. В запрос входит два параметра: логин и пароль. Сейчас создан тестовый пользователь с логином: admin и паролем: admin. В ответ приходит json с уникальным токеном пользователя. В последующем все запросы к базе должны иметь этот token в качестве аргумента.

```
{
  "token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTU3MTE2MjU1NCwiZXhwIjoxNTcxMTcyNTU0fQ.eyJpZCI6MTF9.lAU7dZkII6g3AY81cWDrFlDNCNc_IPQbCeIMR6UlJkozjC5VkOO0enrBW39sI6hEa5GYuatqFgZgaQN28JDnkg"
}
```
 

### Настройка сервиса:


```
git clone https://github.com/maxef23/app_manage

cd app_manage/
python3 -m pip install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
venv/bin/python3 -m pip install -r requirements.txt


mysql
create database plates;

export FLASK_APP=webapp/run.py; flask db init
export FLASK_APP=webapp/run.py; flask db migrate
export FLASK_APP=webapp/run.py; flask db upgrade

INSERT INTO `user` (`id`, `login`, `password`, `name`) VALUES (NULL, 'admin', 'admin', NULL);


```
