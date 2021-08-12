export default {
    async contactPartner(context, payload) {
        const newRequest = {
            // id: new Date().toISOString(),
            // partnerId: payload.partnerId,
            userEmail: payload.email,
            message: payload.message,
        };
        const response = await fetch(
            `https://sportspartner-20854-default-rtdb.europe-west1.firebasedatabase.app/requests/${payload.partnerId}.json`,
            {
                method: 'POST',
                body: JSON.stringify(newRequest)
            });
        const responseData = await response.json();

        if (!response.ok) {
            const error = new Error(responseData.message || 'Error when sending response ');
            throw error;
        }

        newRequest.id = responseData.name;
        newRequest.partnerId = payload.partnerId;

        context.commit('addRequest', newRequest);
    },
    async fetchRequests(context) {
       const partnerId = context.rootGetters.userId;
       const token = context.rootGetters.token;

       const response =  await fetch(
           `https://sportspartner-20854-default-rtdb.europe-west1.firebasedatabase.app/requests/${partnerId}.json?auth=`
           + token );
       const responseData = await response.json();

       if (!response) {
           const error = new Error(responseData.message || 'Error when loading request');
           throw error;
       }

       const requests = [];

       for (const key in responseData) {
           const request = {
               id: key,
               partnerId: partnerId,
               userEmail: responseData[key].userEmail,
               message: responseData[key].message,
           };
           requests.push(request);
       }
       context.commit('setRequests', requests);

    }
};