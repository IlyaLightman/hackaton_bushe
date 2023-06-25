import React from 'react'
import { useParams, useNavigate } from 'react-router-dom'

import { Grid, Container, Typography, Stack, Box } from '@mui/material'
import { blue } from '@mui/material/colors'

import useSelected from './useSelected'

import Couriers from './Couriers'
import Control from './Control'
import Orders from './Orders'
import Routes from './Routes'

const pages = [
	{
		name: 'Курьеры',
		screen: 'couriers',
		PageComponent: Couriers
	},
	{
		name: 'Заказы',
		screen: 'orders',
		PageComponent: Orders
	},
	{
		name: 'Маршруты',
		screen: 'routes',
		PageComponent: Routes
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

	const currentPage = pages.find(page => page.screen == screen)

	return (
		<Stack spacing={4}>
			<HubHeader activeScreen={screen} />
			<Container>
				<Grid container spacing={4} columns={2}>
					<Grid item xs={1}>
						<Box
							sx={{
								background: 'lightgray',
								width: '100%',
								height: 320,
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
