import Vue from 'vue'
import App from './App.vue'
import router from './router'
import {library} from '@fortawesome/fontawesome-svg-core'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import {BootstrapVue} from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import '../scss/custom.scss'

import {
  faFilter,
} from '@fortawesome/free-solid-svg-icons'

library.add(faFilter);

Vue.use(BootstrapVue)
Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
