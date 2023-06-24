import axios from 'axios'

const instance = axios.create({
	baseURL: process.env.BACKEND_URL || 'http://localhost:8000/api',
	headers: {
		'Content-Type': 'application/json',
		'Access-Control-Allow-Origin': '*'
	}
})

// instance.interceptors.request.use(config => {
// 	const token = localStorage.getItem('access_token')
// 	config.headers.Authorization = token ? `Bearer ${token}` : ''
// 	return config
// })

export default instance
