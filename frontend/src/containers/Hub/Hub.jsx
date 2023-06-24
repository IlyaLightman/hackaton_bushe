import React from 'react'
import { useParams } from 'react-router-dom'

const Hub = () => {
	const { id, screen } = useParams() // screen is [null (settings), 'couriers', 'orders', 'routes']

	return (
		<>
			<p>
				Hub {id} {screen}
			</p>
		</>
	)
}

export default Hub
