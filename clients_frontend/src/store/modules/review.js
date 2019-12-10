import api from "../../services/api"

const state = {
	reviews: [],
	review: {},
}


const actions = {
	// client가 작성한 리뷰 
	async getReviews ({ commit }) {
		const token = JSON.parse(localStorage.getItem('user')).token
		const resp = await api.getClientReviews(token)
		const reviews = resp.data.map(review => ({
			'client': review.client,
			'content': review.content,
			'createdAt': review.created_at.split('T')[0] + ' ' + review.created_at.split('T')[1].split('.')[0],
			'feedbacks': review.feedbacks,
			'id': review.id,
			'store': review.store,
			'storeName': review.store_name,
		}))
		commit('setReviews', reviews)
	},
	// store에 작성된 리뷰
	async getStoreReviews ({ commit }, params) {
		const storeId = params
		const resp = await api.getStoreReviews(storeId)
		const reviews = resp.data.map(review => ({
			'client': review.client,
			'author': review.client.slice(0,3) + '***',
			'content': review.content,
			'createdAt': review.created_at.split('T')[0] + ' ' + review.created_at.split('T')[1].split('.')[0],
			'feedbacks': review.feedbacks,
			'id': review.id,
			'store': review.store,
			'storeName': review.store_name,
		}))
		commit('setReviews', reviews)
	},
	async getReview ({ commit }, params) {
		const token = JSON.parse(localStorage.getItem('user')).token
		const resp = await api.getReview(params, token)
		const review = {
			'content': resp.data.content,
			'createdAt': resp.data.created_at.split('T')[0] + ' ' + resp.data.created_at.split('T')[1].split('.')[0],
			'id': resp.data.id,
			'store': resp.data.store,
			'storeName': resp.data.store_name,
		}
		commit('setReview', review)
	},
	async setReview ({ commit }, params) {
		// paramas = {
		// 	'store': storeId,
		// 	'content': content
		// }
		const	token = JSON.parse(localStorage.getItem('user')).token
		const resp = await api.setReview(params, token)
		const review = resp.data.body
		commit('setReview', review)
	},
	async modifyReview ({ commit }, params) {
		const	reviewId = params.reviewId,
					param = { 'content': params.content },
					token = JSON.parse(localStorage.getItem('user')).token
		const resp = await api.modifyReview(reviewId, param, token)
	},
	async deleteReview ({ commit }, params) {
		const	reviewId = params,
					token = JSON.parse(localStorage.getItem('user')).token
		await api.deleteReview(reviewId, token)
	},
}

const mutations = {
	setReviews (state, reviews) {
		state.reviews = reviews
	},
	setReview (state, review) {
		state.review = review
		state.reviews.push(review)
	},
}


  export default {
	namespaced: true,
	state,
	actions,
	mutations
  }
  