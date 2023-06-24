import React from 'react'
import { useParams, useNavigate } from 'react-router-dom'

import { Grid, Container, Typography, Card, Stack } from '@mui/material'
import { blue } from '@mui/material/colors'

import useSelected from './useSelected'
import Couriers from './Couriers'

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
			sx={{ cursor: 'pointer', color: screen == activeScreen ? blue['600'] : 'black' }}
		>
			{name}
		</Typography>
	)
}

const HubHeader = ({ activeScreen }) => {
	return (
		<Container>
			<Grid container justifyContent='center' spacing={4}>
				{pages.map(page => (
					<Grid item key={`${page.screen}`}>
						<LinkTypography hubId={1} activeScreen={activeScreen} {...page} />
					</Grid>
				))}
			</Grid>
		</Container>
	)
}

const Hub = () => {
	const { id, screen } = useParams()

	const { getSelectScreenItemSetter, getSelectedScreenItem } = useSelected()

	return (
		<Stack spacing={4}>
			<HubHeader activeScreen={screen} />
			<Container>
				<Grid container spacing={4} columns={2}>
					<Grid item xs={1}>
						<Card sx={{ background: 'gray', width: '100%', height: '100%' }}>Map</Card>
					</Grid>
					<Grid item xs={1}>
						<Couriers
							hubId={id}
							selectedItem={getSelectedScreenItem('couriers')}
							onSelect={getSelectScreenItemSetter('couriers')}
						/>
					</Grid>
				</Grid>
			</Container>
		</Stack>
	)
}

export default Hub
