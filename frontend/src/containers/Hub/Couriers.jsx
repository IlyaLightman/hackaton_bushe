import React from 'react'

import HubList from '../HubList/HubList'
import { findSelectedItemIndex } from './useSelected'

const getCouriersItems = hubId => {
	return [
		{
			id: 1,
			title: 'Фёдор Достоевский',
			description: '24 км, 03:23',
			statusTitle: 'Маршрут 1',
			statusType: 'process'
		},
		{
			id: 2,
			title: 'Александр Пушкин',
			description: '3 км, 00:31',
			statusTitle: 'Маршрут 2',
			statusType: 'process'
		},
		{
			id: 3,
			title: 'Лев Толстой',
			description: '48 км, 05:12',
			statusTitle: 'Свободен',
			statusType: 'success'
		}
	]
}

const Couriers = ({ hubId, selectedItem, onSelect }) => {
	const couriers = getCouriersItems(hubId)
	const selectedItemIndex = findSelectedItemIndex(couriers, selectedItem)

	return <HubList items={couriers} selectedItemIndex={selectedItemIndex} onClick={onSelect} />
}

export default Couriers
