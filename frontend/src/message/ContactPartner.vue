<template>
    <div>
        <basic-card>
            <form @submit.prevent="submitForm">
                <div>
                    <label for="email">Your Email</label>
                    <input type="text" id="email" v-model.trim="email">
<!--                    <input type="email" id="email" v-model.trim="email">-->
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
    import BasicCard from "../ui/BasicCard";
    import {axiosService} from "../common/api.service";
    export default {
        components: {BasicCard},
        data() {
          return {
            email: '1',
            message: 'undefined',
              receiver: 'admin',
            formIsValid: true
          };
      },
        methods: {
            submitForm() {
              let endpoint = `/api/messages/`;
              let method = 'post';
              const data = {
                  content: this.message,
                  receiver: this.receiver
              };
              axiosService(endpoint, method, data)
                  .then(data => {
                      console.log(data);
                  })
            },
          submitForm_old() {
              this.formIsValid = true;
              if (this.email === '' ||
                  this.message === '') {
                  this.formIsValid = false;
                  return;
              }
              this.$store.dispatch('requests/contactPartner', {
                  partnerId: this.$route.params.id,
                  email: this.email,
                  message: this.message,
              });
              this.$router.replace('/partners');
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