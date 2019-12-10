import api from '@/services/menuApi'

const actions = {
  async postMenu ({ commit }, params) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.postMenu(params, token).catch(error => {
      console.log(error)
    })
  },
  async deleteMenu ({ commit }, menuId) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.deleteMenu(menuId, token).catch(error => {
      console.log(error)
    })
  }
}

export default {
  namespaced: true,
  actions
}