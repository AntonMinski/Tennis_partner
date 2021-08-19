<template>
    <div>
        <form @submit.prevent="registerUser">
            <input type="text" v-model="username" placeholder="username" />
            <input type="password" v-model="password" placeholder="password" />
            <button type="submit">Login</button>
        </form>
        <button @click="getToken">Obtain Token</button>
    </div>
</template>

<script>
    export default {
        data() {
            return{
                username: '',
                password: '',
                token: null,
            };
        },
        methods: {
            getToken() {
                const actionPayload = {
                    username: this.username,
                    password: this.password,
                };
                this.$store.dispatch('getToken', actionPayload);
            },
            registerUser() {
                const actionPayload = {
                    username: this.username,
                    password: this.password,
                };
                this.$store.dispatch('signup', actionPayload);
            },
            Register() {
                const endpoint = "/api/users/register/";
                const method = 'POST';
                const data = {
                    username: this.username,
                    password: this.password,
                };
                this.axiosService(endpoint, method, data)
                    .then(data => {
                        console.log(data);
                        this.token = data.token;
                        console.log(this.token);
                    })
                    .catch(error => console.log(error));


                this.axiosService()
            },
            Auth() {
                const endpoint = "/api/users/token/obtain/";
                const method = 'POST';
                const data = {
                    username: this.username,
                    password: this.password,
                };
                this.axiosService(endpoint, method, data)
                    .then(data => {
                        console.log(data);
                    })
                    .catch(error => console.log(error));
            }
        },


    };
</script>

<style scoped>

</style>