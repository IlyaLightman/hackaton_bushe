import { useState, useCallback } from 'react'
import axios from '../utils/axios'

const useHttp = () => {
	const [loading, setLoading] = useState(false)
	const [error, setError] = useState(null)

	const request = useCallback(async (url, method = 'get', body = null, headers = {}) => {
		setLoading(true)
		try {
			if (body) {
				body = JSON.stringify(body)
				headers['Content-Type'] = 'application/json'
			}

			const response = await axios({
				url,
				method,
				body,
				headers
			})
			const data = response.data

			if (!response.ok) {
				setError(data.errors || 'Something wrong')
			}

			setLoading(false)

			return data
		} catch (err) {
			console.log(err)
			setLoading(false)
			setError(err.message)
		}
	}, [])

	const clearError = useCallback(() => setError(null), [])

	return { loading, request, error, clearError }
}

export default useHttp
