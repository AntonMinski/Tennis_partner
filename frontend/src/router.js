import { createRouter, createWebHistory } from 'vue-router';
import { defineAsyncComponent } from 'vue'

const PartnerDetail = defineAsyncComponent(() => import("./user/PartnerDetail"));
const PartnerRegistration = defineAsyncComponent(() => import("./user/PartnerRegistration"));
const ContactPartner = defineAsyncComponent(() => import("./message/ContactPartner"));
import PartnerList from "./user/PartnerList";
import RequestsReceived from "./message/RequestsReceived";
import NotFound from "./home/NotFound";
import UserAuth from "./user/UserAuth";
import store from './store/index'

import OffersList from "./offer/OffersList";
import OfferDetail from "./offer/OfferDetail";
import OfferEditor from "./offer/OfferEditor";



const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', redirect: '/partners' },
        { path: '/offers', component: OffersList},
        { path: '/offers/:id', component: OfferDetail, props: true,
            children: [
                {path: 'contact', component: ContactPartner, props: true,},
            ]
        },
        { path: '/create_offer', component: OfferEditor, props: true},
        // { path: '/contact/:id', component: ContactPartner, props: true},
        { path: '/partners', component: PartnerList },
        { path: '/partners/:id', component: PartnerDetail, props: true,},
            // children: [
            //     { path: 'contact', component: ContactPartner },
            // ] },
        { path: '/register', component: PartnerRegistration}, // meta: {requiresAuth: true}
        { path: '/messages', component: RequestsReceived, props:true,
            children: [
                {path: 'contact', component: ContactPartner, props: true,}
            ]
        },
        { path: '//auth', component: UserAuth},  // meta: {requiresNone: true}
        { path: '/:notFound(.*)', component: NotFound },
    ],
});

// router.beforeEach(function (to, from, next) {
//     if (to.meta.requiresAuth && store.getters.isAuthenticated) {
//         next('/auth');
//     } else if (to.meta.requiresNone && store.getters.isAuthenticated) {
//         next('/partners');
//     } else {
//         next();
//     }
//
// });

export default router;