import React from 'react'

import { Box, Card, CardMedia, CardContent, Typography, styled } from '@mui/material'

const StyledHubCard = styled(Card)`
	cursor: pointer;
	margin: 1rem;
`

const HubBox = ({ hub }) => {
	return (
		<StyledHubCard>
			<CardMedia
				component='img'
				height='160'
				image='https://i.pinimg.com/736x/89/76/2c/89762c3212c799e451aa61f655bc3261.jpg'
			/>
			<CardContent>
				<Typography variant='h4'>{hub.name}</Typography>
				<Typography variant='h6'>{hub.address}</Typography>
			</CardContent>
		</StyledHubCard>
	)
}

export default HubBox
