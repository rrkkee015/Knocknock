import axios from 'axios'


// const accountsUrl = '/accounts'
// const storesUrl = '/stores'
const accountsUrl = 'https://getick.xyz/accounts'
const storesUrl = 'https://getick.xyz/stores'
const reviewsUrl = 'https://getick.xyz/reviews'

export default {
  signUp (newUser) {
    var params = {
      username: newUser.email,
      password: newUser.password
    }
    return axios.post(`${accountsUrl}/client/signup/`, params)
  },
  signIn (user) {
    var params = {
      username: user.email,
      password: user.password
    }
    return axios.post(`${accountsUrl}/client/login/`, params)
  },
  signOut (token) {
    return axios.get(`${accountsUrl}/client/logout/`, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  },
  userAuth (token) {
    return axios.get(`${accountsUrl}/client/auth/`, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
	},
	
	// Store
	searchStores (lon, lat, hour, d) {
		return axios.get(`${storesUrl}/?loc=${lon},${lat}&hour=${hour}&d=${d}`)
	},
	searchStore (storeId) {
		return axios.get(`${storesUrl}/${storeId}/`)
	},

	// Review
	getReview (reviewId, token) {
		return axios.get(`${reviewsUrl}/${reviewId}/`, {
			headers: {
				'Authorization': 'knock ' + token
			}
		})
	},
	setReview (params, token) {
		return axios.post(`${reviewsUrl}/`, params, {
			headers: {
				'Authorization': 'knock ' + token
			}
		})
	},
	modifyReview (reviewId, params, token) {
		return axios.patch(`${reviewsUrl}/${reviewId}/`, params, {
			headers: {
				'Authorization': 'knock ' + token
			}
		})
	},
	deleteReview (reviewId, token) {
		return axios.delete(`${reviewsUrl}/${reviewId}/`, {
			headers: {
				'Authorization': 'knock ' + token
			}
		})
	},
	getStoreReviews(storeId) {
		return axios.get(`${storesUrl}/${storeId}/reviews/`)
	},

	// client
	getClientReviews (token) {
		return axios.get(`${reviewsUrl}/`, {
			headers: {
				'Authorization': 'knock ' + token
			}
		})
	}
}
