import React from 'react'

import HubList from '../HubList/HubList'
import { findSelectedItemIndex } from './useSelected'
import HubCreateModal from '../HubList/HubCreateModal'

const getRoutesItems = hubId => {
	return [
		{
			id: 1,
			title: 'Маршрут 1',
			description: '15:44 - 16:44',
			statusTitle: 'Лев Толстой'
		},
		{
			id: 2,
			title: 'Маршрут 2',
			description: '15:52 - 16:52',
			statusTitle: 'Александр Пушкин'
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
