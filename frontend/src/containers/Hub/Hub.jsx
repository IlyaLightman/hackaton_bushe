import React from 'react'
import { useParams, useNavigate } from 'react-router-dom'

import { Grid, Container, Typography, Stack, Box } from '@mui/material'
import { blue } from '@mui/material/colors'

import useSelected from './useSelected'

import Couriers from './Couriers'
import Control from './Control'
import Orders from './Orders'
import Routes from './Routes'

import couriersMap from '../../../static/map_couriers.png'
import ordersMap from '../../../static/map_orders.png'
import routesMap from '../../../static/map_routes.png'

const pages = [
	{
		name: 'Курьеры',
		screen: 'couriers',
		PageComponent: Couriers,
		mapImage: couriersMap
	},
	{
		name: 'Заказы',
		screen: 'orders',
		PageComponent: Orders,
		mapImage: ordersMap
	},
	{
		name: 'Маршруты',
		screen: 'routes',
		PageComponent: Routes,
		mapImage: routesMap
	},
	{
		name: 'Управление',
		screen: null,
		PageComponent: Control
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

const HubHeader = ({ hubId, activeScreen }) => {
	return (
		<Container>
			<Grid container justifyContent='center' spacing={4}>
				{pages.map(page => (
					<Grid item key={`${page.screen}`}>
						<LinkTypography hubId={hubId} activeScreen={activeScreen} {...page} />
					</Grid>
				))}
			</Grid>
		</Container>
	)
}

const Hub = () => {
	const { id, screen } = useParams()
	const { getSelectScreenItemSetter, getSelectedScreenItem } = useSelected()

	const currentPage = pages.find(page => page.screen == screen)

	return (
		<Stack spacing={4}>
			<HubHeader hubId={id} activeScreen={screen} />
			<Container>
				<Grid container spacing={4} columns={2}>
					<Grid item xs={1}>
						<Box
							sx={{
								background: 'lightgray',
								backgroundImage: `url(${
									(currentPage && currentPage.mapImage) || ''
								}})`,
								backgroundSize: 'cover',
								width: '100%',
								height: '320px',
								borderRadius: '16px',
								marginBottom: '16px'
							}}
						></Box>
					</Grid>
					<Grid item xs={1}>
						{currentPage && (
							<currentPage.PageComponent
								hubId={id}
								selectedItem={getSelectedScreenItem(screen)}
								onSelect={getSelectScreenItemSetter(screen)}
							/>
						)}
					</Grid>
				</Grid>
			</Container>
		</Stack>
	)
}

export default Hub
