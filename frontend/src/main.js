import { createApp } from 'vue';
import { defineAsyncComponent } from 'vue';

import App from "./App.vue";
import router from "./router.js";
import store from "./store";
import BasicCard from "./ui/BasicCard";
import BasicButton from "./ui/BasicButton";
import BasicBadge from "./ui/BasicBadge";
import BasicIcon from "./ui/BasicIcon";
import apiService from "./mixins/apiService";


const BasicDialog = defineAsyncComponent(() => import("./ui/BasicDialog"));
const LoadingSpinner = defineAsyncComponent(() => import("./ui/LoadingSpinner"));

const app = createApp(App);

app.use(router);
app.use(store);
app.mixin(apiService);

app.component('basic-card', BasicCard);
app.component('basic-button', BasicButton);
app.component('basic-badge', BasicBadge);
app.component('loading-spinner', LoadingSpinner);
app.component('basic-dialog', BasicDialog);
app.component('basic-icon', BasicIcon);

//icons:
// app.use(VuesticPlugin);

app.mount('#app');
