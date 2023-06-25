import { Button, styled } from '@mui/material'
import React from 'react'

import AddIcon from '@mui/icons-material/Add'
import { blue } from '@mui/material/colors'

const HubCreateButtonStyle = styled(Button)`
	height: 48px;
	width: 100%;
	border-radius: 16px;
	margin-bottom: 16px;
	cursor: pointer;
	color: ${blue['500']};
`

const HubCreateButton = ({ onClick }) => {
	return (
		<HubCreateButtonStyle sx={{ bgcolor: 'background.paper' }} onClick={onClick}>
			<AddIcon sx={{ mr: 1 }} />
		</HubCreateButtonStyle>
	)
}

export default HubCreateButton
