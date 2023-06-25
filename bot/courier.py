import operator
from functools import partial

import aiohttp
from aiogram import Bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, User
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


async def acquire_waybill(c: CallbackQuery, button: Button, manager: DialogManager):
    waybill = await fetch('get', f'{API_ROOT}/couriers/{User.get_current().id}/waybill')
    manager.current_context().dialog_data.update(dict(waybill_id=waybill['id']))
    await Bot.get_current().send_message(c.from_user.id, waybill['route_url'])
    await manager.switch_to(MainSG.waybill)


async def release_waybill(c: CallbackQuery, button: Button, manager: DialogManager):
    waybill_id = manager.current_context().dialog_data['waybill_id']
    await fetch('patch', f'{API_ROOT}/waybills/{waybill_id}', payload={'status': 'created'})
    manager.current_context().dialog_data.clear()
    await manager.switch_to(MainSG.root)


async def on_order_select(c: CallbackQuery, select, manager: DialogManager, itme_id: str):
    manager.current_context().dialog_data.update(dict(order_id=itme_id))
    await manager.switch_to(MainSG.order_details)


async def set_order_status(c: CallbackQuery, button: Button, manager: DialogManager, status: str):
    order_id = manager.current_context().dialog_data['order_id']
    await fetch('patch', f'{API_ROOT}/orders/{order_id}', payload={'status': status})
    await manager.switch_to(MainSG.root)

status_label = {
    'picked': '🚚',
    'delivered': '✅',
    'canceled': '❌',
}

async def orders_getter(dialog_manager: DialogManager, **kwargs):
    waybill_id = dialog_manager.current_context().dialog_data['waybill_id']
    waybill = await fetch('get', f'{API_ROOT}/waybills/{waybill_id}')
    orders = waybill['orders']
    for order in orders:
        order['label'] = f'{status_label[order["status"]]}'
    return dict(orders=orders)

async def order_details_getter(dialog_manager: DialogManager,**kwargs):
    order_id = dialog_manager.current_context().dialog_data['order_id']
    waybill = await fetch('get',  f'{API_ROOT}/order/{order_id}')
    orders = waybill['orders']

    return dict(orders=orders)


dialog = Dialog(
    Window(
        Const("Выберите текущий статус"),
        Button(Const("Получить путевой лист"), id="get_order", on_click=acquire_waybill),
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
        Button(Const("Вернуть маршутный лист"), id="get_order", on_click=release_waybill),
        getter=orders_getter,
        state=MainSG.waybill,
    ),
    Window(
        Format("Заказ: {item[id]}"),
        Format("Адрес: {item[address_string]}"),
        Format("Имя: {item[customer_name]}"),
        Format("Телефон: {item[customer_phone]}"),
        Button(Const("✅ Доставлен"), id="get_order", on_click=partial(set_order_status, status='delivered')),
        Button(Const("❌ Отменен"), id="get_order", on_click=partial(set_order_status, status='canceled')),
        Back(Const("↩️ Назад")),
        getter=order_details_getter,
        state=MainSG.order_details,
    )
)