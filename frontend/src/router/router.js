import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Offer from "../views/Offer.vue";
import OfferEditor from "../views/OfferEditor";

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/offers/:slug",
    name: "offer",
    component: Offer,
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
