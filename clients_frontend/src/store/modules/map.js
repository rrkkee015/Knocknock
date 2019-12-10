const state = {
	preCenter: {'lat': 0, 'lng': 0},
	preStores: []
}

const mutations = {
	setPreCenter (state, params) {
		state.preCenter = params
	},
	setPreStores (state, params) {
		state.preStores = params
	}
}

export default {
	namespaced: true,
	state,
	mutations
}