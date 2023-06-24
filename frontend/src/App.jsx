import React from 'react'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'

import { Box } from '@mui/material'

import Hub from './containers/Hub/Hub'

const App = () => {
	return (
		<BrowserRouter>
			<Routes>
				<Route
					path='/'
					element={
						<Box>
							<Link to='/hub'>Hub 1</Link>
						</Box>
					}
				/>
				<Route path='/hub/:id/:screen' element={<Hub />} />
			</Routes>
		</BrowserRouter>
	)
}

export default App
