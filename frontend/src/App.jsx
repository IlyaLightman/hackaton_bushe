import React from 'react'
import { QueryClient, QueryClientProvider } from 'react-query'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'

import { Container, Box, Typography } from '@mui/material'

import Hub from './containers/Hub/Hub'
import Home from './containers/Home/Home'

const queryClient = new QueryClient()

const App = () => {
	return (
		<QueryClientProvider client={queryClient}>
			<BrowserRouter>
				<Container
					maxWidth='sm'
					sx={{ 'text-align': 'center', marginTop: 2, cursor: 'default' }}
				>
					<Typography variant='h3'>Bushe Delivery</Typography>
				</Container>
				<Container>
					<Routes>
						<Route path='/' element={<Home />} />
						<Route path='/hub/:id?/:screen?' element={<Hub />} />
					</Routes>
				</Container>
			</BrowserRouter>
		</QueryClientProvider>
	)
}

export default App
