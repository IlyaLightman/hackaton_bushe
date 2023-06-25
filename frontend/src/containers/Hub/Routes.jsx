import React from 'react'

import HubList from '../HubList/HubList'
import { findSelectedItemIndex } from './useSelected'
import HubCreateModal from '../HubList/HubCreateModal'

const getRoutesItems = hubId => {
	return [
		{
			id: 1,
			title: 'Маршрут 1',
			description: 'Александр Пушкин',
			statusTitle: 'Завершён',
			statusType: 'success'
		},
		{
			id: 2,
			title: 'Маршрут 2',
			description: 'Лев Толстой',
			statusTitle: 'В работе',
			statusType: 'process'
		},
		{
			id: 3,
			title: 'Маршрут 3',
			description: 'Александр Пушкин',
			statusTitle: 'В работе',
			statusType: 'process'
		},
		{
			id: 4,
			title: 'Маршрут 4',
			description: '',
			statusTitle: 'Создан',
			statusType: 'point'
		}
	]
}

const CreateRouteModal = () => <HubCreateModal title='Новый маршрут' />

const Routes = ({ hubId, selectedItem, onSelect }) => {
	const routes = getRoutesItems(hubId)
	const selectedItemIndex = findSelectedItemIndex(routes, selectedItem)

	return (
		<HubList
			items={routes}
			selectedItemIndex={selectedItemIndex}
			onClick={onSelect}
			firstColumnWidth={6}
			withCreate
			CreateButton={CreateRouteModal}
		/>
	)
}

export default Routes
