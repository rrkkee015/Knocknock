import axios from 'axios'

const feedbackUrl = 'https://getick.xyz/feedbacks'

export default {
  postFeedBack (params, token) {
    return axios.post(`${feedbackUrl}/`, params, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  },
  deleteFeedBack (feedbackId, token) {
    console.log()
    return axios.delete(`${feedbackUrl}/` + `${feedbackId}/`, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  }
}
