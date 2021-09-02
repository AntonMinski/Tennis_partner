<template>
    <div>
        <basic-card>
            <form @submit.prevent="submitForm">
                <div>
                    <label for="email">Your Email</label>
                    <input type="text" id="email" v-model.trim="email">
                </div>
                <div>
                    <label for="message">Message</label>
                    <textarea rows="5" id="message" v-model.trim="message"/>
                </div>
                <div class="actions">
                    <basic-button>Send Message</basic-button>
                </div>
                <p v-if="!formIsValid">You try to sent message with empty
                    contact or
                    message field. Playern can't answer you back.</p>
            </form>
        </basic-card>
    </div>
</template>

<script>
    export default {
        // props: ['messageReceiver']
        props: {
            messageReceiver: {
                type: String,
                required: true,
            },
        },
        data() {
          return {
            email: '',
            message: '',
            formIsValid: true
          };
      },
        methods: {
            submitForm() {
                const payload = {
                    endpoint: `/api/messages/`,
                    method: 'post',
                    data: {
                        content: this.message,
                        receiver: this.messageReceiver
                    }
                };

              this.$store.dispatch('axiosRequest', payload)
                  .then(data => {
                      // THIS ACTION IN COSTRUCTION. REEDIRECT + MESSAGE WOULD BE HERE
                      console.log(data);
                  })
            },
        },
    };
</script>

<style scoped>
form {
  margin: 1rem;
  border: 1px solid #ccc;
  border-radius: 12px;
  padding: 1rem;
}

.form-control {
  margin: 0.5rem 0;
}

label {
  font-weight: bold;
  margin-bottom: 0.5rem;
  display: block;
}

input,
textarea {
  display: block;
  width: 100%;
  font: inherit;
  border: 1px solid #ccc;
  padding: 0.15rem;
}

input:focus,
textarea:focus {
  border-color: #3d008d;
  background-color: #faf6ff;
  outline: none;
}

.errors {
  font-weight: bold;
  color: red;
}

.actions {
  text-align: center;
}
</style>