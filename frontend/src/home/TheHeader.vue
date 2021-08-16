<template>
    <header>
        <nav>
            <h1><router-link to="/"> Find a Partner</router-link> </h1>
            <ul>
                <li><router-link to="/partners">All Partners</router-link></li>
                <li class="delim">/</li>
                <li><router-link to="/offers">Offers</router-link></li>
                <li class="delim">/</li>
                <li><router-link to="/messages">Messages</router-link></li>
                <li><router-link to="/login_comp">Login_test</router-link></li>
                <li><a href="/account/login/">Login</a></li>
                <li><a href="/account/register/">Register</a></li>
                <li><a href="/account/logout/">Logout</a></li>
<!--                <li><router-link to="/account/login">Login</router-link></li>-->
<!--                <li><router-link to="/account/register">Register</router-link></li>-->
<!--                <li><router-link to="/account/logout">Logout</router-link></li>-->
<!--                <li v-if="isLoggedIn"><basic-button @click="logout ">Logout</basic-button></li>-->
            </ul>
        </nav>
    </header>
</template>

<script>
    import BasicButton from "../ui/BasicButton";
    export default {
        components: {BasicButton},
        computed: {
            isLoggedIn() {
                return this.$store.getters.isAuthenticated;
            }
        },
        methods: {
           logout() {
               this.$store.dispatch('logout');
               this.$router.replace('/partners')
           },
        },
    }
</script>

<style scoped>
header {
  width: 100%;
  height: 5rem;
  background-color: #565a65;
  display: flex;
  justify-content: center;
  align-items: center;
}

header a {
  text-decoration: none;
    font-weight: 300;
  color: #ffffff;
  display: inline-block;
  padding: 0.75rem 1.5rem;
  border: 1px solid transparent;
}

a:active,
a:hover,
a.router-link-active {
  /*border: 3px solid #81e334;*/
    font-weight: bold;
    color: #81e334;;
}

h1 {
  margin: 0;
}

h1 a {
  color: white;
  margin: 0;
}

h1 a:hover,
h1 a:active,
h1 a.router-link-active {
  border-color: transparent;
}

header nav {
  width: 90%;
  margin: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

header ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

li {
  margin: 0 0.5rem;
}
.delim {
        display: block;
        color: white;
        font-weight: 300;
        font-size: 1.5rem;
        margin: -0.8rem;
    }
</style>