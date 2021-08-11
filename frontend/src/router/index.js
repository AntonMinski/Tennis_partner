import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Offer from "../views/Offer.vue";

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
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
