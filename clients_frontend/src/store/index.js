import Vue from 'vue'
import Vuex from 'vuex'
import toggle from './modules/toggle'
import store from './modules/store'
import review from './modules/review'
import auth from './modules/auth'
import category from './modules/category'
import map from './modules/map'
import notice from './modules/notice'

Vue.use(Vuex)

export default new Vuex.Store({
	modules: {
		toggle,
		store,
		review,
		auth,
		category,
		map,
		notice
	}
})
