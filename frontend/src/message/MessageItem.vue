<template>
    <li>
        <basic-card>
            <p v-if="mode"><span>Sender:</span> {{ sender_name }}</p>
            <p v-else><span>Sent to:</span> {{ receiver_name }}</p>
            <p><span>Content:</span> {{ content }}</p>
            <p><span>Date:</span> {{ created_at }}</p>
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

        },
    };
</script>

<style scoped>

</style>