import { useState, useEffect } from 'react'
import axios from '../../utils/axios'

const useItems = (hubId, screen) => {
	const [items, setItems] = useState([])

	useEffect(() => {
		const fetchItems = async () => {
			const response = await axios.get(`${screen}?hub=${hubId}`)
			console.log(response)
			setItems(response?.data)
		}
		fetchItems()
	}, [screen])

	return items
}

export default useItems
