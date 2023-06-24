Задача - создать сервис

Функциональность:

- получать инфу о заказах
- получать путь следования
- отмечать взятые в работу заказы
- отмечать отданные заказы + комментарии
- закрывать путевой лист
- связь с менеджером

ПОДНЯТЬ ПРОЕКТ

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
