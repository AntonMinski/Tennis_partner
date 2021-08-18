<script>
    import {CSRF_TOKEN} from "./csrf_token";
    import axios from "axios";

    export default {
        name: "apiService",
        data() {
            return {
               token: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI5MzgwNTM4LCJqdGkiOiIxM2VhYWVkOTlmYTM0N2IzOTdiYzE4ODc3YTAwODU2MCIsInVzZXJfaWQiOjJ9.4zQpVm0IL0hazcn6BdEJqxmSMiKh9Qm5NrhwxCCGSo8',
               // token: '333eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyOTM3NTI1NywianRpIjoiMmZhNzI4ODgwNjlhNGRjYmE4MDExNGY0ODM5ODQyMzYiLCJ1c2VyX2lkIjoyfQ.TEWy1d2uvaTqhq1Z2WK9lAJQOqPum21-1CU4VO1yDVs',
            };
        },
        methods: {
            getJSONFetch(response) {
                if (response.status === 204) {
                    return "";
                }
                return response.json();
            },
            responseData(response) {
                if (response.status === 204) {
                    console.log('Response status 204 - No content / undefined data')
                    return "";
                }
                return response.data;
            },
            axiosService(endpoint, method, data) {
                const config = {
                    method: method || "GET",
                    url: endpoint,
                    data: data !== undefined ? JSON.stringify(data) : null, //slf* is data not undefined, then use json.str.... otherwise it is null
                    headers: {
                        'content-type': "application/json",
                        // "Authorization": this.token,
                        'X-CSRFTOKEN': CSRF_TOKEN,
                        Authorization: `Bearer ${this.token}`
                    },
                };
                return axios(config)
                    .then(this.responseData)
                    .catch(err => {
                        console.log(err);
                    })
            },
            apiService(endpoint, method, data) {
                // fetch standart syntax
                const config = {
                    method: method || "GET",
                    body: data !== undefined ? JSON.stringify(data) : null, //slf* is data not undefined, then use json.str.... otherwise it is null
                    headers: {
                        "content-type": "application/json",
                        "X-CSRFTOKEN": CSRF_TOKEN,
                    },
                };
                return fetch(endpoint, config)
                    .then(this.getJSONFetch)
                    .catch((error) => console.log(error))
            },
        },
    };
</script>
