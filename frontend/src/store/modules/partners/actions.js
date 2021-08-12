export default {
    async registerPartner(context, formData) {
        const userId = context.rootGetters.userId;
        // const userId = 'p13';
        const partnerData = {
            firstName: formData.first,
            lastName: formData.last,
            age: formData.age,
            description: formData.desc,
            skillLevel: formData.lvl,
            sportStyles: formData.stl,
        };
        console.log(partnerData)
        console.log(JSON.stringify(partnerData))

        const token = context.rootGetters.token;
        console.log(token)

        const response =  await fetch(`https://sportspartner-20854-default-rtdb.europe-west1.firebasedatabase.app/partners/${userId}.json?auth=`
            + token,
            {
                method: 'PUT',
                body: JSON.stringify(partnerData),
            });

        // const responseData = await response.json();

        if (!response.ok) {
            // error...
        }

        context.commit('registerPartner', {
            ...partnerData,
            id: userId,
        });
    },
    async loadPartners(context, payload) {
        if (!payload.forceRefresh && !context.getters.shouldUpdate) {
            return;
        }

        const response = await fetch(
            `https://sportspartner-20854-default-rtdb.europe-west1.firebasedatabase.app/partners.json`);
        const responseData = await response.json();

        if (!response.ok) {
            const error = new Error(responseData.message || 'Failed to fetch!');
            throw error;
        }

        const partners = [];
        for (const key in responseData) {
            const partner = {
                id: key,
                firstName: responseData[key].firstName,
                lastName: responseData[key].lastName,
                age: responseData[key].age,
                description: responseData[key].description,
                skillLevel: responseData[key].skillLevel,
                sportStyles: responseData[key].sportStyles,
            };
            partners.push(partner);
        }

        context.commit('setPartners', partners);
        context.commit('setFetchTimeStamp')
    }
};