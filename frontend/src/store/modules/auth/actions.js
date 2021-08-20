import {CSRF_TOKEN} from "../../../mixins/csrf_token";

//TODO: 1) actions method with aios instead of old mixin Axios Service;
// 2) add token to method from part 1

let timer;
import axiosService from "../../../mixins/apiService"
import axios from "axios";

export default {
    login(context, payload) {
        return context.dispatch('auth', {
            ...payload,
            mode: 'login'
        });
    },
    signup(context, payload) {
        return context.dispatch('auth', {
            ...payload,
            mode: 'signup'
        });
    },

    auth(context, payload) {
        const mode = payload.mode;
        let endpoint = '/api/users/login/';
        const method = 'POST';
        if (mode === 'signup') {
            endpoint = '/api/users/register/';
        }
        const data = {
            username: payload.username,
            password: payload.password,
        };
        const data2 = data;
        const config = {
                    method: "POST",
                    url: endpoint,
                    data: JSON.stringify(data),
                    headers: {
                        'content-type': "application/json",
                        'X-CSRFTOKEN': CSRF_TOKEN,
                        // Authorization: `Bearer ${this.token}`
                    },
                };

        axios(config)
            .then(response => {
                console.log(response);
                localStorage.setItem('userId', response.data.userId);
                localStorage.setItem('username', response.data.username);

                context.commit('setUser', {
                    username: response.data.username,
                    userId: response.data.userId,
                    // tokenExpiration: responseData.expirationDate,
                });

                // context.commit('setToken', {
                //     token: data.idToken,
                // });
            })
            .catch(err => console.log(err));
            console.log('done auth');
        return context.dispatch('getToken', data);

    },
    getToken(context, payload) {
        console.log('payload.data', payload, payload.username, payload.password);
        const endpoint = "/api/users/token/obtain/";
        const method = 'POST';
        const data = {
            username: payload.username,
            password: payload.password,
        };
        const config = {
            method: "POST",
            url: endpoint,
            data: JSON.stringify(data),
            headers: {
                'content-type': "application/json",
                'X-CSRFTOKEN': CSRF_TOKEN,
                // Authorization: `Bearer ${this.token}`
            },
        };
        axios(config)
            .then(response => {
                localStorage.setItem('token', response.data.access);

                context.commit('setToken', {
                    token: response.data.access,
                });
            })
            .catch(error => console.log(error));
        console.log('get token scs')
    },
    checkLogin(context) {
        const token = localStorage.getItem('token');
        const userId = localStorage.getItem('userId');
        // const tokenExpiration = localStorage.getItem('tokenExpiration')

        // const expiresIn = +tokenExpiration - new Date().getTime();

        // if (expiresIn < 0) {
        //     console.log('token expired');
        //      return;
        // }

        // timer = setTimeout(function () {
        // context.dispatch('autoLogout');
        // }, expiresIn);

        if (token && userId) {
            context.commit('setUser', {
                token: token,
                userId: userId,
                // tokenExpiration: null
            });
            console.log('user has been set', token, userId);
        }
    },

    logout(context) {
        localStorage.removeItem('token');
        localStorage.removeItem('userId');
        // localStorage.removeItem('tokenExpiration');

        clearTimeout(timer);

        context.commit('setUser', {
            token: null,
            userId: null,
        });
    },
    autoLogout(context) {
        context.dispatch('logout');
        context.commit('hadAutoLogout')
    }
};