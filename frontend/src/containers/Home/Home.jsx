import React, { useEffect } from 'react'

import { Grid } from '@mui/material'

import HubBox from '../../components/HubBox'
import useHttp from '../../hooks/http.hook'

const Home = () => {
	const { request } = useHttp()

	useEffect(() => {
		const fetchHubs = async () => {
			const data = await request('/hubs/')
		}
		fetchHubs()
	}, [request])

	const hubs = [
		{ id: 1, name: '1231', address: '123' },
		{ id: 2, name: '4562', address: '456' },
		{ id: 3, name: '1233', address: '123' },
		{ id: 4, name: '4564', address: '456' }
	]

	return (
		<Grid container columns={3}>
			{hubs?.map((hub, index) => (
				<Grid item xs={1} minHeight='1rem' key={hub.id}>
					<HubBox index={index} hub={hub} />
				</Grid>
			))}
		</Grid>
	)
}

export default Home
