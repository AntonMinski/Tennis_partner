export default {
  setUser(state, payload) {
    state.username = payload.username;
    state.userId = payload.userId;
    state.hadAutoLogout = false;
    // state.tokenExpiration = payload.tokenExpiration;
  },
  setToken(state, payload) {
        state.token = payload.token;
  },
  setAutoLogout(state) {
    state.hadAutoLogout = true;
  },
};