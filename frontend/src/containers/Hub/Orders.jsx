import React from 'react'

import HubList from '../HubList/HubList'
import { findSelectedItemIndex } from './useSelected'
import useItems from './useItems'

const getOrdersItems = hubId => {
	return [
		{
			id: 1,
			title: 'M000',
			description: '14:44 - Садовая, 56',
			statusTitle: 'Доставлен',
			statusType: 'success'
		},
		{
			id: 2,
			title: 'M001',
			description: '15:01 - Грибоедова, 21',
			statusTitle: 'Маршрут 2',
			statusType: 'process'
		},
		{
			id: 3,
			title: 'M002',
			description: '15:07 - Некрасова, 1',
			statusTitle: 'В обработке',
			statusType: 'disable'
		}
	]
}

const ordersFrontStatuses = {
	created: {
		title: 'Создан',
		type: 'disable'
	},
	picked: {
		title: 'Маршрут 2',
		type: 'process'
	},
	canceled: {
		title: 'Отменён',
		type: 'error'
	},
	delivered: {
		title: 'Доставлен',
		type: 'success'
	}
}

const mapItemsToOrders = items =>
	items.map(({ id, number, address_string, waybill, status }) => ({
		id,
		title: number,
		description: address_string,
		statusTitle: status !== 'picked' ? ordersFrontStatuses[status].title : waybill,
		statusType: ordersFrontStatuses[status].type
	}))

const Orders = ({ hubId, selectedItem, onSelect }) => {
	const orders = useItems(hubId, 'orders')
	const selectedItemIndex = findSelectedItemIndex(orders, selectedItem)

	return (
		<>
			{orders && (
				<HubList
					items={mapItemsToOrders(orders)}
					selectedItemIndex={selectedItemIndex}
					onClick={onSelect}
					firstColumnWidth={3}
					withCreate
				/>
			)}
		</>
	)
}

export default Orders
