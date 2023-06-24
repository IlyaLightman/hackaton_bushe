import { Divider, List, ListItem } from '@mui/material'
import React from 'react'

const HubList = () => {
	return (
		<List sx={{ width: '100%', bgcolor: 'background.paper' }}>
			<ListItem alignItems='flex-start'>1</ListItem>
			<ListItem alignItems='flex-start'>2</ListItem>
		</List>
	)
}

export default HubList
