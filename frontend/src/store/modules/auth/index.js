import mutations from './mutations.js';
import actions from './actions.js';
import getters from './getters.js';

export default {
  state() {
    return {
      userId: null,
      token: null,
      hadAutoLogout: false,
    };
  },
  mutations,
  actions,
  getters
};