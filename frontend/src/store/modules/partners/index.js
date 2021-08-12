import mutations from './mutations';
import getters from './getters';
import actions from './actions';




export default {
    namespaced: true,
    state() {
        return {
            lastFetch: null,
            partners: [
                {
                    id: 'p1',
                    firstName: 'Ivan',
                    lastName: 'Petrenko',
                    age: 25,
                    sportStyles: ['tennis', 'bike'],
                    description: 'Hi, i am mid-range player. ' +
                        'I preffer training / count-play, 2x2 styles',
                    skillLevel: 3.5,
                },
                  {
                    id: 'p2',
                    firstName: 'Max',
                    lastName: 'Zubenko',
                    age: 32,
                    sportStyles: ['football', 'bike'],
                    description: 'Hi, i am start-range player. ' +
                        'I preffer training and 30-1 hour team challanges',
                    skillLevel: 2,
                },
            ],
        };
    },
        mutations,
        getters,
        actions,
};