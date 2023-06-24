Задача - создать сервис

Функциональность:

- получать инфу о заказах
- получать путь следования
- отмечать взятые в работу заказы
- отмечать отданные заказы + комментарии
- закрывать путевой лист
- связь с менеджером

---
request: GET api/orders - получить список заказов
response:

```json
[
  {
    "id": 1,
    "courier_id": 2,
    "address_id": 3,
    "status": "DELIVERED",
    "products": [
      {
        "id": 1,
        "name": "Булка"
      },
      {
        "id": 2,
        "name": "Кофе"
      }
    ]
  },
  {
    "id": 2,
    "courier_id": 3,
    "address_id": 4,
    "status": "DELIVERED",
    "products": [
      {
        "id": 1,
        "name": "Булка"
      },
      {
        "id": 2,
        "name": "Кофе"
      }
    ]
  }
]
```

---
request: GET api/orders/{orderId} - получить заказ
response:

```json
{
  "id": 1,
  "courier": {
    "id": 1,
    "name": "Магомед"
  },
  "address": {
    "id": 1,
    "info": "Спб большой пс 12"
  },
  "products": [
    {
      "id": 1,
      "name": "Булка"
    },
    {
      "id": 2,
      "name": "Кофе"
    }
  ]
}


```
