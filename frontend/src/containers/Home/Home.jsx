import React from 'react'
import { useQuery } from 'react-query'

import { Grid } from '@mui/material'

import HubBox from '../../components/HubBox'

const Home = () => {
	const { data, isLoading } = useQuery('hubs')

	const hubs = [
		{ name: '123', address: '123' },
		{ name: '456', address: '456' },
		{ name: '123', address: '123' },
		{ name: '456', address: '456' },
		{ name: '123', address: '123' },
		{ name: '456', address: '456' }
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
