<template>
    <div>
        <form @submit.prevent="loginUser">
            <input type="text" v-model="username" placeholder="username" />
            <input type="password" v-model="password" placeholder="password" />
            <button type="submit">LoginUser</button>
        </form>
    </div>
</template>

<script>
    export default {
        data() {
            return{
                username: '',
                password: '',
            };
        },
        methods: {
            loginUser_old() {
                const endpoint = "/api/users/login/";
                const method = 'POST';
                const data = {
                    username: this.username,
                    password: this.password,
                };
                this.axiosService(endpoint, method, data)
                    .then(data => console.log(data))
                    .catch(error => console.log(error));

            },
            loginUser() {
                const actionPayload = {
                    username: this.username,
                    password: this.password,
                };
                this.$store.dispatch('login', actionPayload);
            }
        },


    };
</script>

<style scoped>

</style>