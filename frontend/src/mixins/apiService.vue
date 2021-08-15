<script>
    import {CSRF_TOKEN} from "./csrf_token";
    import axios from "axios";

    export default {
        name: "apiService",
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
                        "content-type": "application/json",
                        "X-CSRFTOKEN": CSRF_TOKEN,
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
