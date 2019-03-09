import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueSocketIO from 'vue-socket.io'

Vue.config.productionTip = false

Vue.use(
  new VueSocketIO({
    debug: true,
    connection: "http://localhost:" + (process.env.PORT | 35433), //'http://127.0.0.1:5000/',
    options: { path: '/socket.io/' }
  })
)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
