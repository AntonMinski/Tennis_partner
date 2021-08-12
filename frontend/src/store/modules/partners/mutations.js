export default {
    registerPartner(state, payload) {
        state.partners.push(payload)
    },
    setPartners(state, payload) {
        state.partners = payload;
    },
    setFetchTimeStamp(state) {
        state.lastFetch = new Date().getTime();
    }
};