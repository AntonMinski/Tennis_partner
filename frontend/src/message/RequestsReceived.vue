<template>
    <div>
        <basic-dialog :show="!!error" title="We received an error..."
                      @close="handleError">
            <p>{{ error }}</p>
        </basic-dialog>
        <section>
            <basic-card>
                <header>
                    <h2>Messages received</h2>
                </header>
                <loading-spinner v-if="isLoading"></loading-spinner>
                <ul v-else-if="hasRequests && !isLoading">
                    <request-item v-for="req in receivedRequests"
                                  :key="req.id" :email="req.userEmail"
                                  :message="req.message">
                    </request-item>
                </ul>
                <h3 v-else>You haven`t received messages yet...</h3>
            </basic-card>
        </section>
    </div>
</template>

<script>
    import RequestItem from "./RequestItem";
    import BasicDialog from "../ui/BasicDialog";

    export default {
        components: {BasicDialog, RequestItem},
        data() {
            return {
                isLoading: false,
                error: null,
            };
        },
        computed: {
            receivedRequests() {
                return this.$store.getters['requests/requests'];
            },
            hasRequests() {
                return this.$store.getters['requests/hasRequests'];
            },
        },
        created() {
            this.loadRequests();
        },
        methods: {
            async loadRequests() {
                this.isLoading = true;
                try {
                    await this.$store.dispatch('requests/fetchRequests');
                } catch (error) {
                    this.error = error.message || 'Something went wrong';
                }
                this.isLoading = false;
            },
            handleError() {
                this.error = null;
            },
        }

    }
</script>

<style scoped>
    header {
        text-align: center;
    }

    ul {
        list-style: none;
        margin: 2rem auto;
        padding: 0;
        max-width: 30rem;
    }

    h3 {
        text-align: center;
    }
</style>