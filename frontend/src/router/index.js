import Vue from 'vue'
import VueRouter from 'vue-router'
import cp_gpu_status from '../components/cp_gpu_status'
import login from '../components/ll'
import ListVideo from "../components/ListVideo";
import {TokenService} from "../storage/service";

Vue.use(VueRouter)

const requireAuth = () => (from, to, next) => {
    const isAuthenticated = TokenService.getToken()
    console.log('requireAuth',isAuthenticated)
    if (isAuthenticated) return next()
    next({ path: '/login' })

}
const routes = [
    {
        path: '/',
        name: 'home',
        component: cp_gpu_status,
        beforeEnter: requireAuth()

    },
    {
        path: '/login',
        name: 'login',
        component: login

    },
    {
        path: '/gpu',
        name: 'gpu',
        component: cp_gpu_status,
        beforeEnter: requireAuth()
    },
    {
        path: '/about',
        name: 'about',
        component: ListVideo,
        beforeEnter: requireAuth()
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    }
]

const router = new VueRouter({
    routes
})

export default router
