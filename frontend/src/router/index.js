import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
history: createWebHistory(),
routes: [
    {
        path: '/',
        name: 'home',
        component: () => import('@/views/Home.vue')
    },
    {
        path: '/biographic',
        name: 'biographic',
        component: () => import('@/views/Biographic.vue')
    },
    {
        path: '/blog/:blog_id',
        name: 'blog',
        component: () => import('@/views/blog/Detail.vue')
    },
    {
        path: '/blogs',
        name: 'blogs',
        component: () => import('@/views/blog/List.vue')
    },
    {
        path: '/book/:product_id',
        name: 'book',
        component: () => import('@/views/book/Detail.vue')
    },
    {
        path: '/books',
        name: 'books',
        component: () => import('@/views/books/List.vue')
    },
    {
        path: '/',
        name: 'contact',
        component: () => import('@/views/Contact.vue')
    },
]
});

export default router
export const routes = router.options.routes;