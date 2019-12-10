import Vue from 'vue'
import Vuex from 'vuex'

import auth from './modules/auth'
import drawer from './modules/drawer'
import postEvent from './modules/postEvent'
import store from './modules/store'
import menu from './modules/menu'
import feedback from './modules/feedback'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
    drawer,
    postEvent,
    store,
    menu,
    feedback
  }
})
