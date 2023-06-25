import React from 'react'

import { findSelectedItemIndex } from './useSelected'
import useItems from './useItems'

import HubList from '../HubList/HubList'

const mapItemsToCouriers = items =>
	items.map(({ id, name, distance_progress, time_progress, current_waybill, status }) => ({
		id,
		title: name,
		description: `${distance_progress}, ${time_progress}`,
		statusTitle: status === 'busy' ? current_waybill : 'Свободен',
		statusType: status === 'busy' ? 'process' : 'success'
	}))

const Couriers = ({ hubId, selectedItem, onSelect }) => {
	const couriers = useItems(hubId, 'couriers')
	const selectedItemIndex = findSelectedItemIndex(couriers, selectedItem)

	return (
		<>
			{couriers && (
				<HubList
					items={mapItemsToCouriers(couriers)}
					selectedItemIndex={selectedItemIndex}
					onClick={onSelect}
					withCreate
				/>
			)}
		</>
	)
}

export default Couriers
