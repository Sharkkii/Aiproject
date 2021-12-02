import VueRouter from "vue-router"
import VIndexPage from "../components/pages/VIndexPage.vue"

const routes = [
  {
    path: "",
    component: VIndexPage
  }
]

const router = new VueRouter({
  routes: routes
})

export default router;