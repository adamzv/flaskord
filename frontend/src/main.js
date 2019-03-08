import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
//import io from 'socket.io-client'
import VueSocketIO from 'vue-socket.io'

//export const socket = io('http://127.0.0.1:5000/')

Vue.config.productionTip = false

Vue.use(
  new VueSocketIO({
    debug: true,
    connection: 'http://127.0.0.1:5000/',
    options: { path: '/socket.io/' }
  })
)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
