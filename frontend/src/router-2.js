import { createRouter, createWebHistory } from "vue-router";
import HomePage from "./offer/OffersList.vue";
import OfferPage from "./offer/OfferDetail.vue";
import OfferEditor from "./offer/OfferEditor";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  {
    path: "/offers/:id",
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
