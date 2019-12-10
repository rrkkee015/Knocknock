import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false

new Vue({
  async created () {
    if ('user' in localStorage) {
      store.commit('auth/logOutCondition')
      await store.dispatch('auth/userAuth')
      if (this.$store.state.auth.err) {
        store.commit('auth/initError')
        localStorage.removeItem('user')
        router.push('/').catch(err => {
          console.log('이동하려는 위치가 현재와 동일합니다. / ' + err.message)
        })
      }
    } else {
      await store.commit('auth/logInCondition')
      if (this.$router.currentRoute.name !== 'main') {
        router.push('/').catch(err => {
          console.log('이동하려는 위치가 현재와 동일합니다. / ' + err.message)
        })
      }
    }
  },
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
