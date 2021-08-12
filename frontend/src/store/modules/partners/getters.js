export default {
    partners(state) {
        return state.partners;
    },
    hasPartners(state) {
        return state.partners && state.partners.length > 0;
    },
    isRegistered(_, getters, _2, rootGetters) {
        const partners = getters.partners;
        const userId = rootGetters.userId
        return partners.some(partner => partner.id === userId); // returns True if it find any user id in partners

    },
    shouldUpdate(state) {
        const lastFetch = state.lastFetch;
        if (!lastFetch) {
            return true;
        }
        const currentTimeStamp = new Date().getTime();
        return (currentTimeStamp - lastFetch) / 1000 > 60;  // true, if more > 1 minute ago
    }
};