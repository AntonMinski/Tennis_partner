<template>
    <div>
        <basic-dialog :show="!!error" title="We received an error..."
                      @close="handleError">
            <p>{{ error }}</p>
        </basic-dialog>
        <div>
            <button @click="switchReceivedMode" :class="[ receive_mode ? 'active_now' : 'outline']">Received</button>
            <button @click="switchSentMode" :class="[ !receive_mode ? 'active_now' : 'outline']">Sent</button>
        </div>
        <section>
            <basic-card>
                <header>
                    <h2 v-if="receive_mode">Messages received</h2>
                    <h2 v-else>Messages sent</h2>
                </header>
            </basic-card>
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
    import RequestItem from "./RequestItem";
    import { axiosService } from "../common/api.service";
    import MessageItem from "./MessageItem";

    export default {
        components: {MessageItem, RequestItem},
        data() {
            return {
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
                return this.$store.getters['requests/requests']
            },
            hasRequests() {
                return this.$store.getters['requests/hasRequests']
            },
        },
        created() {
            // this.loadRequests();
            this.switchReceivedMode();
            // this.switchReceivedMode()
        },
        methods: {
            getMessagesList() {
                let endpoint = this.endpoint;

                if (this.next) {
                    endpoint = this.next;
                }

                axiosService(endpoint)
                    .then(data => {
                        this.messages_list.push(...data.results);
                        if (data.next) {
                            this.next = data.next;
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
      border: 1px solid #585858;
      color: #585858;
      cursor: pointer;
      border-radius: 10px;
      margin-right: 0.5rem;
      display: inline-block;
    }

    button:hover,
    button:active {
      background-color: #8ace60;
      border-color: #adce60;
        color: white;
        font-size: 1.2rem;
    }

    .flat {
      background-color: transparent;
      color: #787878;
      border: none;
    }

    .outline {
      background-color: transparent;
      border-color: #585858;
      color: #585858;
    }

    .active_now {
        background-color: #8ace60;
        color: white;
        /*border: #8ace60;*/
    }

      .active_now:hover {
        color: #444444;
          font-size: 1.1rem;
          border: 3px solid #bef300;
        /*border: #8ace60;*/
    }

    .flat:hover,
    .flat:active,
    .outline:hover,
    .outline:active {
      background-color: #8ace60;
        border: #8ace60;
    }

</style>