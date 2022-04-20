import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegistrationView from '../views/RegistrationView.vue'
import LoginView from '../views/LoginView.vue'
import AddCarView from '../views/AddCarView.vue'
import ExploreView from '../views/ExploreView.vue'
import CarView from '../views/CarView.vue'
import UserView from '../views/UserView.vue'

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
      path:'/cars/new',
      name:'/cars/new',
      component: AddCarView
    },
    {
      path: '/explore',
      name: '/explore',
      component:ExploreView
    },
    {
      path: '/cars/:car_id',
      name: '/cars/:car_id',
      component:CarView
    },
    {
      path: '/users/:user_id',
      name: '/users/:user_id',
      component:UserView
    }
  ]
})

export default router
