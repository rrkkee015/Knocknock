const state = {
  signupShow: false,
	headerShow: true,
	navDrawerShow: false,
	filterShow: false,
	registerReviewModalShow: false,
}

const mutations = {
  toggleSignup (state, toggle) {
    state.signupShow = toggle
  },
  toggleHeader (state, toggle) {
    state.headerShow = toggle
	},
	toggleNavDrawer (state, toggle) {
		state.navDrawerShow = toggle
	},
  toggleFilter (state, toggle) {
	  state.filterShow = toggle
	},
	toggleRegisterReviewModal (state, toggle) {
		state.registerReviewModalShow = toggle 
	}
}

export default {
  namespaced: true,
  state,
  mutations
}
