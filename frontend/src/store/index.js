import { createStore } from "vuex";
import partnersModule from './modules/partners/index';
import requestsModule from './modules/requests/index';
import authModule from './modules/auth/index';

const store = createStore({
    modules: {
        partners: partnersModule,
        requests: requestsModule,
        auth: authModule,
    },

});


export default store;

