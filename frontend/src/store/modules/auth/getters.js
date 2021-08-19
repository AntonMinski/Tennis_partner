export default {
  userId(state) {
    return state.userId;
  },
  username(state) {
    return state.username;
  },
  token(state) {
    return state.token;
  },
  isAuthenticated(state) {
    return !!state.token;
  },
  hadAutoLogout(state) {
    return state.hadAutoLogout
  },
};