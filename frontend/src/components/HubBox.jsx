import React from 'react'
import { useNavigate } from 'react-router-dom'

import { Card, CardMedia, CardContent, Typography, styled } from '@mui/material'

const bushe_images = [
	'https://avatars.mds.yandex.net/get-altay/2812564/2a0000017089a44e442252f100040cd2767b/XXL',
	'https://avatars.mds.yandex.net/get-altay/2056672/2a0000016d776d189012e5d3c299ad8fcb78/XXXL',
	'https://avatars.mds.yandex.net/get-altay/2006845/2a0000016e7eccb5c9fae5ac01e3e39b5930/XXXL',
	'https://avatars.mds.yandex.net/get-altay/4435487/2a000001779493f164fac51f48e0f764bf05/XXXL'
]

const StyledHubCard = styled(Card)`
	cursor: pointer;
	margin: 1rem;
`

const HubBox = ({ index, hub }) => {
	const navigate = useNavigate()

	const handleClick = () => navigate(`/hub/${hub.id}/couriers`)

	return (
		<StyledHubCard onClick={handleClick}>
			<CardMedia component='img' height='160' image={bushe_images[index]} />
			<CardContent>
				<Typography variant='h6'>{hub.name}</Typography>
				<Typography variant='caption'>{hub.address}</Typography>
			</CardContent>
		</StyledHubCard>
	)
}

export default HubBox
