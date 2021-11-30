import Vue from "vue"
import VueRouter from "vue-router"
import router from "./router/router.js"
import App from "./App"

Vue.use(VueRouter)

const app = new Vue({
  router,
  el: "#app",
  components: {
    App
  },
  template: "<App/>"
})