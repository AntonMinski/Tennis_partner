<template>
    <the-header></the-header>
<!-- to make router animation/transition, here adding v-slot and :is-->
    <router-view v-slot="slotProps">
        <transition name="route" mode="out-in">
            <component :is="slotProps.Component"></component>
        </transition>
    </router-view>
</template>

<script>
    import TheHeader from "./home/TheHeader";

    export default {
        components: {
            TheHeader,
        },
        computed: {
            hadAutoLogout() {
              return this.$store.getters.hadAutoLogout;
            },
        },
        created() {
            this.$store.dispatch('tryLogin');
        },
        watch: {
            hadAutoLogout(curValue, oldValue) {
                if(curValue && curValue !== oldValue ) {
                    this.$router.replace('/partners');
                }
            },
        },
    };
</script>

<style scoped>
    * {
        box-sizing: border-box;
    }

    html {
        font-family: sans-serif;
    }

    body {
        margin: 0;
    }

    .route-enter-from {
        opacity: 0;
        transform: translateY(-30px);
    }

    .route-leave-to {
        opacity: 0;
        transform: translateY(30px);
    }

    .route-enter-active {
        transition: all 0.3s ease-out;
    }

    .route-leave-active {
        transition: all 0.3s ease-in
    }

    .route-enter-to,
    .route-leave-from {
        opacity: 1;
        transform: translateY(0);
    }

</style>