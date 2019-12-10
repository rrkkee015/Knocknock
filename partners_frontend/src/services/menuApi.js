import axios from 'axios'

const menuUrl = 'https://getick.xyz/menus'

export default {
  postMenu (params, token) {
    return axios.post(`${menuUrl}/`, params, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  },
  deleteMenu (menuId, token) {
    return axios.delete(`${menuUrl}/` + `${menuId}/`, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  }
}
