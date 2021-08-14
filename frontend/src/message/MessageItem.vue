<template>
    <li>
<!--        <div>-->
<!--            <a :href="emailLink">{{ email }}</a>-->
<!--        </div>-->
        <basic-card>
        <p>{{ id }}</p>
        <p>{{ content }}</p>
        <p>{{ created_at }}</p>
            <basic-button>Answer</basic-button>
            </basic-card>

    </li>
</template>

<script>
    import BasicCard from "../ui/BasicCard";
    import BasicButton from "../ui/BasicButton";
    export default {
        components: {BasicButton, BasicCard},
        props: ['id', 'content', 'created_at'],
        computed: {
            // emailLink() {
            //     return 'mailto:' + this.email;
            // },
        },
    };
</script>

<style scoped>

</style>