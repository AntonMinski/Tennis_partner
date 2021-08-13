import { CSRF_TOKEN } from "./csrf_token";
import axios from "axios";

function getJSONFetch(response) {
  if (response.status === 204) {
    return "";
  }
  return response.json();
}

function responseData(response) {
  if (response.status === 204) {
    console.log('Response status 204 - No content / undefined data')
    return "";
  }
  return response.data;
}

function axiosService(endpoint, method, data) {
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
      .then(responseData)
      .catch(err => {
        console.log(err);
      })

}

function apiService(endpoint, method, data) {
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
    .then(getJSONFetch)
    .catch((error) => console.log(error))
}

export { axiosService, apiService };
// export { apiService };
