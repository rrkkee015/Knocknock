import api from '@/services/feedbackApi'

const actions = {
  async postFeedBack ({ commit }, params) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.postFeedBack(params, token).catch(error => {
      console.log(error)
    })
  },
  async deleteFeedBack ({ commit }, feedBackId) {
    var token = JSON.parse(localStorage.getItem('user')).token
    await api.deleteFeedBack(feedBackId, token).catch(error => {
      console.log(error)
    })
  }
}

export default {
  namespaced: true,
  actions
}
