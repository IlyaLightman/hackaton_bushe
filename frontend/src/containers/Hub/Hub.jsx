import React from 'react'
import { useParams, useNavigate, Link } from 'react-router-dom'

import { Grid, Container, Typography } from '@mui/material'

const pages = [
	{
		name: 'Курьеры',
		screen: 'couriers'
	},
	{
		name: 'Заказы',
		screen: 'orders'
	},
	{
		name: 'Маршруты',
		screen: 'waybills'
	}
]

const LinkTypography = ({ hubId, screen, activeScreen, name }) => {
	const navigate = useNavigate()

	return (
		<Typography
			variant='h5'
			onClick={() => navigate(`/hub/${hubId}/${screen}`)}
			sx={{ cursor: 'pointer', color: screen === activeScreen ? 'royalblue' : 'black' }}
		>
			{name}
		</Typography>
	)
}

const HubHeader = ({ hub, activeScreen }) => {
	return (
		<Container>
			<Grid container spacing={4}>
				<Grid item>
					<Typography variant='h5' sx={{ cursor: 'default' }}>
						{hub?.name || 'Hub'}:
					</Typography>
				</Grid>
				{pages.map(page => (
					<Grid item>
						<LinkTypography hubId={1} activeScreen={activeScreen} {...page} />
					</Grid>
				))}
			</Grid>
		</Container>
	)
}

const Hub = () => {
	const { id, screen } = useParams() // screen is [null (settings), 'couriers', 'orders', 'routes']

	return (
		<>
			<HubHeader activeScreen={screen} />
			<Container>
				<p>Hahub</p>
				<p>
					Hub {id} {screen}
				</p>
			</Container>
		</>
	)
}

export default Hub
