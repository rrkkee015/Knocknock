import axios from 'axios'

// const partnerUrl = '/partner/stores'
const partnerUrl = 'https://getick.xyz/partner'
const storesUrl = 'https://getick.xyz/stores'
const feedbacksUrl = 'https://getick.xyz/feedbacks'

export default {
  getAllStores (token) {
    return axios.get(`${partnerUrl}/` + 'stores/', {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  },
  getOneStore (storeId, token) {
    return axios.get(`${storesUrl}/` + storeId + '/', {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  },
  enrollStore (params, token) {
    // let form = new FormData()
    // form.append('is_new', params.is_new)
    // form.append('company_name', params.company_name)
    // form.append('business_registration_number', params.business_registration_number)
    // form.append('representative_name', params.representative_name)
    // form.append('business_address', params.business_address)
    // form.append('registration_image', params.registration_image)
    return axios.post(`${partnerUrl}/` + 'regist/', params, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  },
  searchStore (name) {
    return axios.get(`${storesUrl}/search/`, {
      params: {
        name: name
      }
    })
  },
  editStoreDescrip (params) {
    var id = params.id
    var token = JSON.parse(localStorage.getItem('user')).token
    delete params.id
    return axios.patch(`${partnerUrl}/` + 'stores/' + `${id}/`, params, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  },
  postFeedBack (data, token) {
    return axios.post(`${feedbacksUrl}/`, data, {
      headers: {
        'Authorization': 'knock ' + token
      }
    }).catch(error => {
      console.log(error)
    })
  },
  getAllFeedBacks (data, token) {
    return axios.get(`${feedbacksUrl}/`, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  },
  getAllMenus (params, token) {
    return axios.get(`${storesUrl}/` + `${params}/` + 'menus/', {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  },
  postMenu (params, token) {
    var storeId = params.store
    delete params.store
    return axios.post(`${storesUrl}/` + `${storeId}/` + 'menus/', params, {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  },
  getReviews (storeId, token) {
    return axios.get(`${storesUrl}/` + `${storeId}/` + 'reviews/', {
      headers: {
        'Authorization': 'knock ' + token
      }
    })
  }
}
