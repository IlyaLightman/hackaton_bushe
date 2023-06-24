import operator
from functools import partial

import aiohttp
from aiogram import Bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery
from aiogram_dialog import Window, Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Button, Select, Back, Column
from aiogram_dialog.widgets.text import Const, Format

API_ROOT = 'http://localhost:8000/api'


async def fetch(method, url, payload=None):
    async with aiohttp.ClientSession() as session:
        if payload:
            async with getattr(session, method)(url, payload=payload) as response:
                return await response.json()
        else:
            async with getattr(session, method)(url) as response:
                return await response.json()


class MainSG(StatesGroup):
    root = State()
    waybill = State()
    order_details = State()


async def get_waybill(c: CallbackQuery, button: Button, manager: DialogManager):
    # waybill = await fetch('get', API_ROOT + '/waybill')
    waybill = {'id': 1, 'route_url': 'ya.ru'}
    url = 'https://yandex.ru/maps/2/saint-petersburg/?ll=30.395113%2C59.844421&mode=routes&rtext=59.841269%2C30.384075~59.853284%2C30.352418~59.859356%2C30.392814~59.841868%2C30.381387&rtt=auto&ruri=~~~&z=13.09'
    manager.current_context().dialog_data.update(dict(waybill_id=waybill['id']))
    await Bot.get_current().send_message(c.from_user.id, waybill['route_url'])
    await manager.switch_to(MainSG.waybill)


async def return_waybill(c: CallbackQuery, button: Button, manager: DialogManager):
    waybill_id = manager.current_context().dialog_data['waybill_id']
    await fetch('put', f'{API_ROOT}/waybill/{waybill_id}', payload={'status': 'returned'})
    manager.current_context().dialog_data.clear()
    await manager.switch_to(MainSG.root)


async def on_order_select(c: CallbackQuery, select, manager: DialogManager, itme_id: str):
    manager.current_context().dialog_data.update(dict(order_id=itme_id))
    await manager.switch_to(MainSG.order_details)


async def set_order_status(c: CallbackQuery, button: Button, manager: DialogManager, status: str):
    order_id = manager.current_context().dialog_data['order_id']
    await fetch('put', f'{API_ROOT}/orders/{order_id}', payload={'status': status})
    await manager.switch_to(MainSG.root)


async def orders_getter(**kwargs):
    waybill = await fetch('get', API_ROOT + '/waybills')
    orders = waybill['orders']
    mock = dict(orders=[dict(id=1, status='picked'), dict(id=2, status='delivered')])
    return dict(orders=mock)


status_label = {
    'picked': '🚚',
    'delivered': '✅',
    'canceled': '❌',
}


async def order_details_getter(**kwargs):
    waybill = await fetch('get', API_ROOT + '/waybill')
    orders = waybill['orders']
    orders = [(order['id'], f'{status_label[order["status"]]}') for order in orders]
    return dict(orders=orders)


dialog = Dialog(
    Window(
        Const("Выберите текущий статус"),
        Button(Const("Получить путевой лист"), id="get_order", on_click=get_waybill),
        state=MainSG.root,
    ),
    Window(
        Const("Лови маршрут и список заказов"),
        Column(
            Select(
                Format("{item[label]} Заказ {item[id]}"),
                id="s_orders",
                item_id_getter=operator.itemgetter('id'),
                items="orders",
                on_click=on_order_select,
            )),
        Button(Const("Вернуть маршутный лист"), id="get_order", on_click=return_waybill),
        getter=orders_getter,
        state=MainSG.waybill,
    ),
    Window(
        Format("Заказ: {item[id]}"),
        Format("Адрес: {item[address_string]}"),
        Format("Имя: {item[customer_name]}"),
        Format("Телефон: {item[customer_phone]}"),
        Button(Const("Доставлен"), id="get_order", on_click=partial(set_order_status, status='delivered')),
        Button(Const("Отменен"), id="get_order", on_click=partial(set_order_status, status='canceled')),
        Back(Const("Назад")),
        getter=order_details_getter,
        state=MainSG.order_details,
    )
)
