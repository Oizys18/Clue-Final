import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueSession from 'vue-session'
import Vuesax from 'vuesax'
import 'vuesax/dist/vuesax.css'

Vue.config.productionTip = false
Vue.use(VueSession)
Vue.use(Vuesax, {
  theme: {
    colors: {
      success:'rgba(227, 227, 0, 0.5)'
    }
  }
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
