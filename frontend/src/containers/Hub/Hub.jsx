import React from 'react'
import { useParams, useNavigate, Link } from 'react-router-dom'

import { Grid, Container, Typography, Card, Stack } from '@mui/material'

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
		screen: 'routes'
	},
	{
		name: 'Управление',
		screen: null
	}
]

const LinkTypography = ({ hubId, screen, activeScreen, name }) => {
	const navigate = useNavigate()

	return (
		<Typography
			variant='h5'
			onClick={() => navigate(`/hub/${hubId}/${screen || ''}`)}
			sx={{ cursor: 'pointer', color: screen == activeScreen ? 'royalblue' : 'black' }}
		>
			{name}
		</Typography>
	)
}

const HubHeader = ({ hub, activeScreen }) => {
	return (
		<Container>
			<Grid container justifyContent='center' spacing={4}>
				{/* <Grid item>
					<Typography variant='h5' sx={{ cursor: 'default' }}>
						{hub?.name || 'Hub'}:
					</Typography>
				</Grid> */}
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
	const { id, screen } = useParams()

	return (
		<Stack spacing={4}>
			<HubHeader activeScreen={screen} />
			<Container>
				<Grid container spacing={4} columns={2}>
					<Grid item xs={1}>
						<Card sx={{ background: 'gray', width: '100%', height: '100%' }}>Map</Card>
					</Grid>
					<Grid item xs={1}>
						map
					</Grid>
				</Grid>
			</Container>
		</Stack>
	)
}

export default Hub
