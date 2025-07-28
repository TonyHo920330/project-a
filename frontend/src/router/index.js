import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue' // ✅ 加上這行匯入元件

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
