import React, { useEffect } from 'react'

import { Grid } from '@mui/material'

import HubBox from '../../components/HubBox'
import useHttp from '../../hooks/http.hook'

const Home = () => {
	const { request } = useHttp()

	useEffect(() => {
		const fetchHubs = async () => {
			const data = await request('/hubs/')
			console.log(data)
		}
		fetchHubs()
	}, [request])

	const hubs = [
		{ name: '1231', address: '123' },
		{ name: '4562', address: '456' },
		{ name: '1233', address: '123' },
		{ name: '4564', address: '456' },
		{ name: '1235', address: '123' },
		{ name: '4566', address: '456' }
	]

	return (
		<Grid container columns={3}>
			{hubs.map(hub => (
				<Grid xs={1} minHeight='1rem' key={hub?.name}>
					<HubBox hub={hub} />
				</Grid>
			))}
		</Grid>
	)
}

export default Home
