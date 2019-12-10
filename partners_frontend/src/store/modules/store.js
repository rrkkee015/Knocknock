import api from '@/services/storeApi'

const state = {
  allStores: [],
  oneStore: [],
  error: null,
  storeInfo: {},
  totalOptions: ['주차', '발렛파킹', '포장', '예약', '단체석', '무선 인터넷', '남/녀 화장실 구분', '배달', '방문접수/출장', '장애인 편의시설', '반려동물 동반', '24시간', '드라이브스루', '유아시설(놀이방)'],
  possibleOptions: [],
  searchResult: [],
  isNew: false,
  storeId: null,
  searchOn: false,
  allReviews: [],
  allFeedBacks: [],
  allMenus: []
}

const mutations = {
  regiAllStores (state, data) {
    state.allStores = data
  },
  regiOneStore (state, data) {
    state.oneStore = data
  },
  setError (state, data) {
    state.error = data
  },
  initError (state) {
    state.error = null
  },
  setInfo (state) {
    state.possibleOptions = []
    for (var i = 0; i < state.oneStore.data.options.length; i++) {
      state.possibleOptions.push(state.oneStore.data.options[i])
    }
    state.storeInfo = {
      id: state.oneStore.data.id,
      storeName: state.oneStore.data.name,
      description: state.oneStore.data.description,
      priceAvg: state.oneStore.data.price_avg.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","),
      reviewCnt: state.oneStore.data.review_cnt.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ","),
      roadAddr: state.oneStore.data.road_addr,
      contact: state.oneStore.data.contact,
      options: state.possibleOptions,
      mainCategory: state.oneStore.data.category.main_category,
      subCategory: state.oneStore.data.category.sub_category,
      business_hours: state.oneStore.data.business_hours,
      tags: state.oneStore.data.tags
    }
  },
  searchResponse (state, resp) {
    state.searchResult = resp.data
  },
  setIsNew (state) {
    state.isNew = true
  },
  initIsNew (state) {
    state.isNew = false
  },
  setStoreId (state, id) {
    state.storeId = id
  },
  initStoreId (state) {
    state.storeId = null
  },
  setSearchOn (state) {
    state.searchOn = true
  },
  initSearchOn (state) {
    state.searchOn = false
  },
  setAllReviews (state, data) {
    data.sort(function (a, b) {
      return a.id < b.id ? -1 : a.name < b.name ? 1 : 0
    })
    state.allReviews = data
  },
  setAllFeedBacks (state, data) {
    state.allFeedBacks = data
  },
  initAllFeedBacks (state) {
    state.allFeedBacks = []
  },
  setAllMenus (state, data) {
    state.allMenus = data
  }
}

const actions = {
  async getAllStores ({ commit }) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.getAllStores(token).then(resp => {
      commit('regiAllStores', resp)
    }).catch(error => {
      commit('setError', error)
    })
  },
  async getOneStore ({ commit }, payload) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.getOneStore(payload, token).then(resp => {
      commit('setAllReviews', resp.data.reviews)
      commit('regiOneStore', resp)
    }).catch(error => {
      commit('setError', error)
    })
  },
  async enrollStore ({ commit }, payload) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.enrollStore(payload, token).catch(error => {
      commit('setError', error)
    })
  },
  async searchStore ({ commit }, name) {
    await api.searchStore(name).then(resp => {
      commit('searchResponse', resp)
    })
  },
  async editStoreDescrip ({ commit }, params) {
    await api.editStoreDescrip(params).catch(error => {
      console.log(error)
    })
  },
  async getAllFeedBacks ({ commit }, params) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.getAllFeedBacks(params, token).then(resp => {
      commit('setAllFeedBacks', resp.data)
    }).catch(error => {
      console.log(error)
    })
  },
  async getAllMenus ({ commit }, params) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.getAllMenus(params, token).then(resp => {
      commit('setAllMenus', resp.data)
    }).catch(error => {
      console.log(error)
    })
  },
  async postMenu ({ commit }, params) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.postMenu(params, token).catch(error => {
      console.log(error)
    })
  },
  async getReviews ({ commit }, storeId) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.getReviews(storeId, token).then(resp => {
      for (var i = 0; i < resp.data.length; i++) {
        resp.data[i].reviewTextBox = false
      }
      commit('setAllReviews', resp.data)
    }).catch(error => {
      console.log(error)
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
