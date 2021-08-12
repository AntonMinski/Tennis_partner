import { createRouter, createWebHistory } from "vue-router";
import HomePage from "./home/HomePage.vue";
import OfferPage from "./offer/OfferPage.vue";
import OfferEditor from "./offer/OfferEditor";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  {
    path: "/offers/:slug",
    name: "offer",
    component: OfferPage,
    props: true,
  },
  {
    path: "/create_offer",
    name: "offer_editor",
    component: OfferEditor,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
