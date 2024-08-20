FastAPI сервис, реализующий операции над сущностью User с полями - id, ФИО.
Сервис предполагает:

- создание User,

- изменение User,

- получение по id,

- удаление User.

Запуск:
- изменить .env.example на .env и заполнить настройками в:
```bash
app/.env.example
app/core/initialiser/.env.example
```

- установка зависемостей:
```shell
cd app && pip install -r requirements.txt 
```
- запуск web версии:
```shell
 cd app && python web_app.py
```
- запуск консольной версии:

```shell
 cd app && python console_app.py command "params"
```
где command:
- get - получение по id
- create - создание
- delete - удаление
- update - обновление

**Пример**:

```shell
 cd app && python console_app.py get "Arnold"
```