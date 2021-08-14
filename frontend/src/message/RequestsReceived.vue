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
                <ul v-else>
                    <message-item v-if="receive_mode"
                                  v-for="message in messages_received_list"
                                  :key="message.id"
                                  :id="message.id"
                                  :content="message.content"
                                  :created_at="message.created_at">
                    </message-item>
                    <message-item v-else
                                  v-for="message in messages_sent_list"
                                  :key="message.id"
                                  :id="message.id"
                                  :content="message.content"
                                  :created_at="message.created_at">
                    </message-item>
                    <button v-if="next_received & receive_mode" @click="getReceivedList">Load more</button>
                    <button v-if="next_sent & !receive_mode" @click="getSentList">Load more</button>
                </ul>

<!--                <h5 v-else>You haven`t received messages yet...</h5>-->
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
                messages_received_list: [],
                messages_sent_list: [],
                next_received: null,
                next_sent: null,
            };
        },
        computed: {
            switchReceivedMode() {
                this.receive_mode = true;
                this.next_received = false;
                this.messages_sent_list = [];
                this.getReceivedList();
                // console.log(this.receive_mode);
                // console.log(this.next_sent);
            },
            switchSentMode() {
                this.receive_mode = false;
                this.next_sent = false;
                this.messages_received_list = [];
                this.getSentList();
                console.log('now this next_sent = ', this.next_sent, ' and');
                console.log('now this receive_mode = ', this.receive_mode);
            },
            receivedRequests() {
                return this.$store.getters['requests/requests'];
            },
            hasRequests() {
                return this.$store.getters['requests/hasRequests'];
            },
        },
        created() {
            // this.loadRequests();
            this.getReceivedList();
            // this.getSentList();
        },
        methods: {

            getReceivedList() {
                let endpoint = 'api/messages_received/';
                if (this.next_received) {
                    endpoint = this.next_received;
                }
                axiosService(endpoint)
                    .then(data => {
                        this.messages_received_list.push(...data.results);
                        console.log(this.messages_received_list);
                        if (data.next) {
                            console.log('data_next_received')
                            this.next_received = data.next;
                        } else {
                            this.next_received = null;
                        }
                    });

            },

            getSentList() {
                let endpoint = 'api/messages_sent/';
                if (this.next_sent) {
                    endpoint = this.next_sent;
                }
                axiosService(endpoint)
                    .then(data => {
                        this.messages_sent_list.push(...data.results);
                        console.log(this.messages_sent_list);
                        if (data.next) {
                            console.log('data_next_sent')
                            this.next_sent = data.next;
                            console.log(this.next_sent)
                        } else {
                            this.next_sent = null;
                        }
                    });

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