export default {
  setUser(state, payload) {
    state.token = payload.token;
    state.userId = payload.userId;
    state.hadAutoLogout = false;
    // state.tokenExpiration = payload.tokenExpiration;
  },
  setAutoLogout(state) {
    state.hadAutoLogout = true;
  },
};