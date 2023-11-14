import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/AppHome.vue'
import Statistiques from '../views/Statistiques.vue'

const MAIN_TITLE = 'TED'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/statistiques',
    name: 'Statistiques',
    component: Statistiques,
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env?.BASE_URL || ''),
  routes,
})

router.beforeEach((to) => { // Cf. https://github.com/vueuse/head pour des transformations avancées de Head
  const specificTitle = to.meta.title ? `${to.meta.title} - ` : ''
  document.title = `${specificTitle}${MAIN_TITLE}`
})

export default router
