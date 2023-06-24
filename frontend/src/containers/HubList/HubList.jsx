import React, { useMemo } from 'react'

import { Block, CheckCircleOutline, Clear, FlipCameraAndroid } from '@mui/icons-material'
import { Typography, List, ListItem, Stack, styled, Grid } from '@mui/material'
import { amber, blueGrey, green } from '@mui/material/colors'

const statusColorByType = {
	success: green['600'],
	process: amber['600'],
	disable: blueGrey['300'],
	error: 'red'
}

const getStatusIconByType = (type, color = 'black') =>
	({
		success: <CheckCircleOutline fontSize='small' sx={{ color }} />,
		process: <FlipCameraAndroid fontSize='small' sx={{ color }} />,
		disable: <Clear fontSize='small' sx={{ color }} />,
		error: <Block fontSize='small' sx={{ color }} />
	}[type])

const StatusTag = ({ title, type }) => {
	const color = useMemo(() => statusColorByType[type] || 'black', [type])

	return (
		<Stack direction='row' alignItems='center' spacing={1}>
			{getStatusIconByType(type, color)}
			<Typography variant='body1' sx={{ color }}>
				{title}
			</Typography>
		</Stack>
	)
}

const HubListItemStyled = styled(ListItem)`
	height: 48px;
	border-radius: 16px;
	margin-bottom: 16px;
`

const HubListItem = ({
	id,
	title = '',
	description = '',
	selected,
	onClick,
	children,
	...props
}) => {
	return (
		<HubListItemStyled
			alignItems='flex-start'
			sx={{ bgcolor: 'background.paper', cursor: 'pointer' }}
			onClick={() => onClick(id)}
			selected={selected}
			{...props}
		>
			<Grid
				container
				direction='row'
				justifyContent='center'
				alignItems='center'
				sx={{ height: '100%' }}
				columns={20}
			>
				<Grid item xs={8}>
					<Typography variant='subtitle1'>{title}</Typography>
				</Grid>
				<Grid item xs={6}>
					<Typography variant='body1' sx={{ color: blueGrey['300'] }}>
						{description}
					</Typography>
				</Grid>
				<Grid item xs={6}>
					{children}
				</Grid>
			</Grid>
		</HubListItemStyled>
	)
}

const HubList = ({ items, selectedItemIndex, onClick }) => {
	return (
		<List sx={{ width: '100%', padding: 0 }}>
			{items?.map(({ statusTitle, statusType, id, ...itemProps }, index) => (
				<HubListItem
					id={id}
					{...itemProps}
					selected={index === selectedItemIndex}
					onClick={onClick}
					key={id}
				>
					<StatusTag title={statusTitle} type={statusType} />
				</HubListItem>
			))}
			{/* <HubListItem title='Лев Толстой' description='25 км, 03:44' selected>
				<StatusTag title='Маршрут 2' type='process' />
			</HubListItem>
			<HubListItem title='Фёдор Достоевский' description='32 км, 05:12'>
				<StatusTag title='Маршрут 1' type='process' />
			</HubListItem>
			<HubListItem title='Филипп Дик' description='4 км, 00:37'>
				<StatusTag title='Свободен' type='success' />
			</HubListItem> */}
		</List>
	)
}

export default HubList
