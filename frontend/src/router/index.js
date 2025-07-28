import { createRouter, createWebHistory } from 'vue-router'
import OrderProductView from '../views/OrderProductView.vue'
import CheckoutView from '../views/CheckoutView.vue'

const routes = [
    { path: '/order', component: OrderProductView },
    { path: '/checkout', component: CheckoutView }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
