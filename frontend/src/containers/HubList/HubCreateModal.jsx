import React, { useState } from 'react'
import { styled, Box, Modal, Typography } from '@mui/material'
import HubCreateButton from './HubCreateButton'

const ModalBoxStyle = styled(Box)`
	position: absolute;
	top: 20%;
	left: 50%;
	transform: translate(-50%, -50%);
	width: 400px;
	border-radius: 16px;
	box-shadow: 24;
`

const HubCreateModal = ({ title = '' }) => {
	const [open, setOpen] = useState(false)

	return (
		<>
			<HubCreateButton onClick={() => setOpen(true)} />
			<Modal
				open={open}
				onClose={() => setOpen(false)}
				aria-labelledby='modal-modal-title'
				aria-describedby='modal-modal-description'
			>
				<ModalBoxStyle sx={{ bgcolor: 'background.paper', p: 4 }}>
					<Typography id='modal-modal-title' variant='h6' component='h2'>
						{title}
					</Typography>
				</ModalBoxStyle>
			</Modal>
		</>
	)
}

export default HubCreateModal
