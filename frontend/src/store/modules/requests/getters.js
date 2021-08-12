export default {
    requests(state, _, _2, rootGetters) {
        const partnerId = rootGetters.userId;
        return state.requests.filter(req => req.partnerId === partnerId);
    },
    hasRequests(_, getters) {
        return getters.requests && getters.requests.length > 0;
    },
};