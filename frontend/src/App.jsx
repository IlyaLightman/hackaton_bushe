import React from 'react'
import { BrowserRouter, Routes, Route, useNavigate } from 'react-router-dom'

import { Container, Typography } from '@mui/material'

import Hub from './containers/Hub/Hub'
import Home from './containers/Home/Home'

const Header = () => {
	const navigate = useNavigate()

	const handleGoHome = () => navigate('/')

	return (
		<Container
			maxWidth='sm'
			sx={{ 'text-align': 'center', marginTop: 2, marginBottom: 1, cursor: 'pointer' }}
			onClick={handleGoHome}
		>
			<Typography variant='h4'>Bushe Delivery</Typography>
		</Container>
	)
}

const App = () => {
	return (
		<BrowserRouter>
			<Header />
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
