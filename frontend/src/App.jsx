import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

import { Container, Typography } from '@mui/material'

import Hub from './containers/Hub/Hub'
import Home from './containers/Home/Home'

const App = () => {
	return (
		<BrowserRouter>
			<Container
				maxWidth='sm'
				sx={{ 'text-align': 'center', marginTop: 2, marginBottom: 1, cursor: 'default' }}
			>
				<Typography variant='h4'>Bushe Delivery</Typography>
			</Container>
			<Container>
				<Routes>
					<Route path='/' element={<Home />} />
					<Route path='/hub/:id?/:screen?' element={<Hub />} />
				</Routes>
			</Container>
		</BrowserRouter>
	)
}

export default App
