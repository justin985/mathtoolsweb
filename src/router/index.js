import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import SosTools from '../views/SosTools.vue'
import LagrangeCal from '../views/LagrangeCal.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/sostools',
      name: 'sostools',
      component: SosTools
    },
    {
      path: '/lagrange',
      name: 'lagrange',
      component: LagrangeCal
    }
  ]
})

export default router