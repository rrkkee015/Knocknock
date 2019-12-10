import api from "../../services/api"

const state = {
	stores: [],
	store: {
		options: [],
		reviews: {
			feedbacks: []
		},
		tags: [],
		menus: [],
	},
	// parmas for searchStores API
	storeSearchHour: 0,
	storeSearchLoc: [0, 0],
	storeSearchDistance: 0,
}

const getters = {
	reviewsLen (state) {
		return state.store.reviews.length
	},
	menus (state) {
		let menus = state.store.menus
		for (var i=0; i < menus.length; i++) {
			if (menus[i].price) {
				menus[i].price = menus[i].price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
			}
		}
		state.store.menus = menus
		return state.store.menus
	},
	businessHours (state) {
		if(state.store.businessHours) {
			const businessHours = state.store.businessHours.map(bizHour => ({
				'day': bizHour.day,
				'isDayoff': bizHour.is_dayoff, 
				'start': bizHour.start,
				'end': bizHour.end,
				'startBreak': bizHour.start_break,
				'endBreak': bizHour.end_break,
				'lastOrder': bizHour.last_order
			}))
			state.store.businessHours = businessHours
		}
		return state.store.businessHours
	},
}

const actions = {
	async getStores ({ commit }) {
		const lon = state.storeSearchLoc[1],
					lat = state.storeSearchLoc[0],
					hour = state.storeSearchHour,
					d = state.storeSearchDistance
		const resp = await api.searchStores(lon, lat, hour, d)
		const stores = resp.data.map(store => ({
			'addr': store.addr,
			'mainCategory': store.category.main_category,
			'subCategory': store.category.sub_category,
			'category': store.category,
			'commonAddr': store.common_addr,
			'contact': store.contact,
			'distance': store.distance,
			'id': store.id,
			'lat': store.lat,
			'leftTime': store.left_time,
			'lon': store.lon,
			'name': store.name,
			'priceAvg': store.price_avg,
			'roadAddr': store.road_addr,
			'thumbnail': store.thumbnail,
		}))
		commit('setStores', stores)
	},
	async getSingleStore ({ commit }, storeId) {
		const resp = await api.searchStore(storeId)
		const store = {
			'addr': resp.data.addr,
			'businessHours': resp.data.business_hours,
			'mainCategory': resp.data.category.main_category,
			'subCategory': resp.data.category.sub_category,
			'commonAddr': resp.data.common_addr,
			'contact': resp.data.contact,
			'description': resp.data.description,
			'id': resp.data.id,
			'lat': resp.data.lat,
			'lon': resp.data.lon,
			'menus': resp.data.menus,
			'name': resp.data.name,
			'options': resp.data.options,
			'partner': resp.data.partner,
			'priceAvg': resp.data.price_avg,
			'reviewCnt': resp.data.review_cnt,
			'reviews': resp.data.reviews,
			'roadAddr': resp.data.road_addr,
			'tags': resp.data.tags,
			'thumbnail': resp.data.thumbnail,
			'viewCnt': resp.data.view_cnt,
		}
		// tags가 있으면 split해서 arr로 만들기
		if (store.tags.length) {
			store.tags = store.tags.split(",")
		}
		// priceAvg가 있으면 세자리마다 ',' 찍기
		if (store.priceAvg) {
			store.priceAvg = store.priceAvg.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
		}
		commit('setSingleStore', store)
	}
}

const mutations = {
	setStores (state, stores) {
		state.stores = stores 
	},
	setSingleStore (state, store) {
		state.store = store
	},
	getStoreSearchHour (state, param) {
		state.storeSearchHour = param
	},
	getStoreSearchLoc (state, param) {
		state.storeSearchLoc = param
	},
	getStoreSearchDistance (state, param) {
		state.storeSearchDistance = param
	},
}

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations,
  }
  