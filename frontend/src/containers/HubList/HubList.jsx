import React, { useMemo } from 'react'

import {
	Block,
	CheckCircleOutline,
	Clear,
	FlipCameraAndroid,
	AddLocationOutlined
} from '@mui/icons-material'
import { Typography, List, ListItem, Stack, styled, Grid } from '@mui/material'
import { amber, blueGrey, green } from '@mui/material/colors'

import HubCreateButton from './HubCreateButton'

const statusColorByType = {
	success: green['600'],
	process: amber['600'],
	disable: blueGrey['300'],
	point: blueGrey['300'],
	error: 'red'
}

const getStatusIconByType = (type, color = 'black') =>
	({
		success: <CheckCircleOutline fontSize='small' sx={{ color }} />,
		process: <FlipCameraAndroid fontSize='small' sx={{ color }} />,
		disable: <Clear fontSize='small' sx={{ color }} />,
		point: <AddLocationOutlined fontSize='small' sx={{ color }} />,
		error: <Block fontSize='small' sx={{ color }} />
	}[type])

const StatusTag = ({ title, type }) => {
	const color = useMemo(() => statusColorByType[type] || 'black', [type])

	return (
		<Stack direction='row' alignItems='center' spacing={1}>
			{getStatusIconByType(type, color)}
			<Typography variant='body1' sx={{ color, userSelect: 'none' }}>
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
	firstColumnWidth = 8,
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
				<Grid item xs={firstColumnWidth}>
					<Typography variant='subtitle1' sx={{ userSelect: 'none' }}>
						{title}
					</Typography>
				</Grid>
				<Grid item xs={20 - 6 - firstColumnWidth}>
					<Typography variant='body1' sx={{ color: blueGrey['300'], userSelect: 'none' }}>
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

const HubList = ({
	items,
	selectedItemIndex,
	onClick,
	firstColumnWidth,
	withCreate,
	CreateButton
}) => {
	return (
		<List sx={{ width: '100%', padding: 0 }}>
			{items?.map(({ statusTitle, statusType, id, ...itemProps }, index) => (
				<HubListItem
					id={id}
					{...itemProps}
					selected={index === selectedItemIndex}
					onClick={onClick}
					key={id}
					firstColumnWidth={firstColumnWidth}
				>
					<StatusTag title={statusTitle} type={statusType} />
				</HubListItem>
			))}
			{withCreate && (CreateButton ? <CreateButton /> : <HubCreateButton />)}
		</List>
	)
}

export default HubList
