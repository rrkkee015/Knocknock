import Vue from 'vue'
import VueRouter from 'vue-router'

import authPage from '../pages/AuthPage'
import storePage from '../pages/StorePage'
import storeDetailPage from '../pages/StoreDetailPage'
import storeSearchPage from '../pages/StoreSearchPage'
import registerFormPage from '../pages/RegisterFormPage'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: authPage, name: 'authPage' },
    { path: '/store', component: storePage, name: 'storePage' },
    { path: '/store/register', component: storeSearchPage, name: 'storeSearchPage' },
    { path: '/store/form', component: registerFormPage, name: 'registerFormPage' },
    { path: '/store/:storeId', component: storeDetailPage, name: 'storeDetailPage' }
  ]
})

export default router
