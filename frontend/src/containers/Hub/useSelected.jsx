import { useState } from 'react'

const useSelected = () => {
	const [selected, setSelected] = useState({})

	const getSelectScreenItemSetter = screen => itemId => {
		if (selected[screen] !== itemId) {
			setSelected({ ...selected, [screen]: itemId })
		} else {
			setSelected({ ...selected, [screen]: undefined })
		}
	}

	const getSelectedScreenItem = screen => selected[screen]

	return { getSelectScreenItemSetter, getSelectedScreenItem }
}

export const findSelectedItemIndex = (items, selectedItem) => {
	console.log(items)
	return items?.findIndex(item => item.id === selectedItem)
}

export default useSelected
