<template>
    <li>
<!--        <div>-->
<!--            <a :href="emailLink">{{ username }}</a>-->
<!--        </div>-->
        <p>{{ message }}</p>
    </li>
</template>

<script>
    export default {
        props: ['message'],
        computed: {
            emailLink() {
                return 'mailto:' + this.email;
            },
        },
    };
</script>

<style scoped>

</style>