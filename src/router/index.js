import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegistrationView from '../views/RegistrationView.vue'
import LoginView from '../views/LoginView.vue'
import AddCarView from '../views/AddCarView.vue'
import Logout from '../components/Logout.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/register',
      name: 'register',
      component: RegistrationView
    },
    {
      path: '/login',
      name: '/login',
      component: LoginView
    },
    {
      path: '/logout',
      name: '/logout',
      component: Logout
    },
    {
      path:'/cars/new',
      name:'/cars/new',
      component: AddCarView
    }
  ]
})

export default router
