import React from 'react'

import HubList from '../HubList/HubList'
import { findSelectedItemIndex } from './useSelected'
import HubCreateModal from '../HubList/HubCreateModal'
import useItems from './useItems'

const waybillsFrontStatuses = {
	created: {
		title: 'Создан',
		type: 'disable'
	},
	appointed: {
		title: 'Назначен',
		type: 'point'
	},
	in_progress: {
		title: 'В работе',
		type: 'process'
	},
	completed: {
		title: 'Доставлен',
		type: 'success'
	}
}

const mapItemsToWaybills = items =>
	items.map(({ id, number, courier: { name }, status }) => ({
		id,
		title: number,
		description: name,
		statusTitle: waybillsFrontStatuses[status].title,
		statusType: waybillsFrontStatuses[status].type
	}))

const CreateRouteModal = () => <HubCreateModal title='Новый маршрут' />

const Routes = ({ hubId, selectedItem, onSelect }) => {
	const routes = useItems(hubId, 'waybills')
	const selectedItemIndex = findSelectedItemIndex(routes, selectedItem)

	return (
		<>
			{routes && (
				<HubList
					items={mapItemsToWaybills(routes)}
					selectedItemIndex={selectedItemIndex}
					onClick={onSelect}
					firstColumnWidth={6}
					withCreate
					CreateButton={CreateRouteModal}
				/>
			)}
		</>
	)
}

export default Routes
