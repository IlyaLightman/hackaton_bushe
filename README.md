Задача - создать сервис

Функциональность:

- Получать инфу о заказах
- Получать путь следования
- Отмечать взятые в работу заказы
- Отмечать отданные заказы + комментарии
- Закрывать путевой лист
- Связь с менеджером

ПОДНЯТЬ ПАРУСА

```shell
docker-compose up -d --build --force-recreate app
```

НАКАТИТЬ СИД

```shell
docker-compose exec -it app python backend/manage.py seed
```

УДАЛИТЬ ЗАПИСИ ИЗ БД

```shell
docker-compose exec -it app python backend/manage.py delete
```
