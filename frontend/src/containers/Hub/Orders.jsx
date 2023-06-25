import React from 'react'

import HubList from '../HubList/HubList'
import { findSelectedItemIndex } from './useSelected'

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

const Orders = ({ hubId, selectedItem, onSelect }) => {
	const orders = getOrdersItems(hubId)
	const selectedItemIndex = findSelectedItemIndex(orders, selectedItem)

	return (
		<HubList
			items={orders}
			selectedItemIndex={selectedItemIndex}
			onClick={onSelect}
			firstColumnWidth={3}
			withCreate
		/>
	)
}

export default Orders
