<template>
    <li>
<!--        <div>-->
<!--            <a :href="emailLink">{{ username }}</a>-->
<!--        </div>-->
        <basic-card>
<!--        <p>{{ id }}</p>-->
        <p v-if="mode">Sender: {{ sender_name }}</p>
        <p v-else>Sent to: {{ receiver_name }}</p>
        <p>{{ content }}</p>
        <p>{{ created_at }}</p>
            <basic-button link :to="contactLink">Answer</basic-button>
            <router-view :message-receiver="receiver_name"></router-view>
            </basic-card>

    </li>
</template>

<script>
    import ContactPartner from "../message/ContactPartner";
    export default {
        components: {ContactPartner},
        props: ['id', 'content', 'created_at', 'sender', 'receiver', 'mode',
        'sender_name', 'receiver_name'],
        computed: {
          contactLink() {
             return this.$route.path + '/contact';
          },
            // emailLink() {
            //     return 'mailto:' + this.username;
            // },
        },
    };
</script>

<style scoped>

</style>