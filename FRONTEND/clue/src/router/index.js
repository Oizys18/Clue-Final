import Vue from 'vue'
import VueRouter from 'vue-router'
import Quiz from '../views/Quiz.vue'
import About from '../views/About.vue'
import QuizList from '../views/QuizList.vue'
import Login from '../views/Login.vue'
import Userdetail from '../views/Userdetail.vue'
import Suspicious from '../views/Suspicious.vue'
import PageNotFound from '../views/PageNotFound.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Quiz',
    component: Quiz
  },
  {
    path: '/quiz',
    name: 'Quiz',
    component: Quiz
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/quizlist',
    name: 'QuizList',
    component: QuizList
  },
  {
    path: '/suspicious',
    name: 'Suspicious',
    component: Suspicious
  },
  {
    path: '/userdetail',
    name: 'Userdetail',
    component: Userdetail
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '*',
    component: PageNotFound,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_ENV,
  routes
})

export default router
