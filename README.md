Задача - создать сервис

Функциональность:

- получать инфу о заказах
- получать путь следования
- отмечать взятые в работу заказы
- отмечать отданные заказы + комментарии
- закрывать путевой лист
- связь с менеджером

---
Модели:

User - менеджер

- id: int
- name: varchar
- login: varchar
- password: varchar

Hub - точка выдачи заказов:

- id: int
- name: varchar
- lat: float
- lon: float
- address: varchar
- since: time
- till: time

Courier - курьер:

- id: int
- name: varchar
- hub_id: foreign key hub.id

Order - заказ:

- id: int
- number: varchar unique
- status: varchar
- hub: foreign key hub.id
- lat: float
- lon: float
- address: varchar
- comment: varchar nullable

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
