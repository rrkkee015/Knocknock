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
      await store.dispatch('auth/userAuth')
      if (this.$store.state.auth.error) { // 토큰을 가지고 있지만 이상한 토큰일 때
        store.commit('auth/initError')
        localStorage.removeItem('user')
        router.push('/').catch(error => {
          console.log('이동하려는 위치가 현재와 동일합니다. / ' + error.message)
        })
      }
    } else { // 그냥 토큰이 없을 때
      if (this.$router.currentRoute.name !== 'authPage') {
        router.push('/').catch(error => {
          console.log('이동하려는 위치가 현재와 동일합니다. / ' + error.message)
        })
      }
    }
  },
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
