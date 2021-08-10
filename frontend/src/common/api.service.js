import { CSRF_TOKEN } from "./csrf_token";

function getJSON(response) {
    if (response.status === 204 ) {
        return '';
    }
    return response.json();
}

function apiService(endpoint, method, data) {
    // fetch standart syntax
    const config = {
        method: method || 'GET',
        body: data !== undefined ? JSON.stringify(data) : null,  //slf* is data not undefined, then use json.str.... otherwise it is null
        headers: {
            'content-type': 'application/json',
            'X-CSRFTOKEN': CSRF_TOKEN
        }
    };
    return fetch(endpoint, config)
        .then(getJSON)
        .catch(error => console.log(error))
}

export { apiService };