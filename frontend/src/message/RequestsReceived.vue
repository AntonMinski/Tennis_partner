<template>
    <div>

        <basic-dialog :show="!!error" title="We received an error..."
                      @close="handleError">
            <p>{{ error }}</p>
        </basic-dialog>

        <div class="tab-container">
        <basic-card>
            <div class="tab-set">
            <button @click="switchReceivedMode" :class="[ receive_mode ? 'active_now' : 'outline']">Received</button>
            <button @click="switchSentMode" :class="[ !receive_mode ? 'active_now' : 'outline']">Sent</button>
            </div>
        </basic-card>
            </div>


        <section>

                <loading-spinner v-if="isLoading"></loading-spinner>
                <ul v-else-if="messages_list">
                    <message-item v-for="message in messages_list"
                                  :key="message.id"
                                  :id="message.id"
                                  :sender="message.sender"
                                  :sender_name="message.sender_name"
                                  :receiver="message.receiver"
                                  :receiver_name="message.receiver_name"
                                  :content="message.content"
                                  :created_at="message.created_at"
                                  :mode="receive_mode">
                    </message-item>
                    <button v-if="next" @click="getMessagesList">Load more</button>
                </ul>
                <h5 v-else>You haven`t received messages yet...</h5>
        </section>
    </div>
</template>

<script>
    import MessageItem from "./MessageItem";
    export default {
        components: {MessageItem},
        data() {
            return {
                value: 'One',
                isLoading: false,
                error: null,
                receive_mode: true,
                messages_list: [],
                next: null,
                endpoint_receive: 'api/messages_received/',
                endpoint_sent: 'api/messages_sent/',
                endpoint: '',
            };
        },
        computed: {
            receivedRequests() {
                this.$store.dispatch('axiosRequest', {endpoint: this.endpoint})
                return this.$store.getters['requests/requests']
            },
            hasRequests() {
                return this.$store.getters['requests/hasRequests']
            },
        },
        created() {
            this.switchReceivedMode();
        },
        methods: {
            getMessagesList() {
                let endpoint = this.endpoint;

                if (this.next) {
                    endpoint = this.next;
                }

                this.$store.dispatch('axiosRequest', {endpoint:endpoint})
                    .then(response => {
                        console.log(response.data);
                        this.messages_list.push(...response.data.results);
                        if (response.data.next) {
                            this.next = response.data.next;
                        } else {
                            this.next = null;
                        }
                    });
            },
            getInitialState() {
                this.messages_list = [];
                this.next = null;
                this.getMessagesList()
            },
            switchReceivedMode() {
                this.receive_mode = true;
                this.endpoint = this.endpoint_receive;
                this.getInitialState();
            },
            switchSentMode() {
                this.receive_mode = false;
                this.endpoint = this.endpoint_sent;
                this.getInitialState();
            },

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
    .header-block {
        margin: 0 34.5%;
    }

    .tab-container {
        display: block;
        width: 50%;
        margin: 0 auto;
        padding: 0 15%;
    }

    .tab-set {
        padding: 0;
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
    }


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

    button {
      text-decoration: none;
      padding: 0.5rem 1.5rem;
      font: inherit;
      background-color: #e8e8e8;
      color: #585858;
      cursor: pointer;
      margin-right: 0.5rem;
      display: inline-block;
      border: none;
      border-radius: 0;
    }


    .outline {
      background-color: transparent;
      border: none;
      color: #585858;
        border-radius: 0;
    }

    .active_now,
    .active_now:focus,
    .active_now:active {
        /*background-color: #8ace60;*/
        outline:none !important;
        background-color: transparent;
        color: 787878;
        border: none;
        font-weight: 600;
        border-bottom: #81e334 solid 2px;
        border-radius: 0;
        /*border: #8ace60;*/
    }

      .active_now:hover {
        outline:none !important;
        color: #444444;
          font-size: 1.1rem;
          border-bottom: 3px solid #81e334;
          border-radius: 0;
        /*border: #8ace60;*/
    }

    .flat:hover,
    .flat:active,
    .outline:hover,
    .outline:active {
        outline:none !important;
        font-size: 1.1rem;
      /*background-color: #8ace60;*/
      /*  border: #8ace60;*/
    }

    button::-moz-focus-inner {
  border: 0;
}

</style>