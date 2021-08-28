<template>
  <div>
    <basic-dialog :show="!!error" title="An error occurred" @close="handleError">
      <p>{{ error }}</p>
    </basic-dialog>
    <basic-dialog :show="isLoading" title="Authenticating..." fixed>
      <loading-spinner></loading-spinner>
    </basic-dialog>
    <basic-card>
      <form @submit.prevent="submitForm">
        <div class="input-block">
          <label for="username">Name</label>
          <input type="username" id="username" v-model.trim="username" />
        </div>
        <div class="input-block">
          <label for="password">Password</label>
          <input type="password" id="password" v-model.trim="password" />
        </div>
        <p
          v-if="!formIsValid"
        >Please enter a valid email and password (must be at least 6 characters long).</p>
        <basic-button>{{ submitButtonCaption }}</basic-button>
        <basic-button type="button" mode="flat" @click="switchAuthMode">{{ switchModeButtonCaption }}</basic-button>
      </form>
    </basic-card>
  </div>
</template>

<script>
import BasicButton from "../ui/BasicButton";
export default {
  components: {BasicButton},
  data() {
    return {
      username: '',
      password: '',
      formIsValid: true,
      mode: 'login',
      isLoading: false,
      error: null,
    };
  },
  computed: {
    submitButtonCaption() {
      if (this.mode === 'login') {
        return 'Login';
      } else {
        return 'Signup';
      }
    },
    switchModeButtonCaption() {
      if (this.mode === 'login') {
        return 'Signup instead';
      } else {
        return 'Login instead';
      }
    },
  },
  methods: {
    submitForm() {
      this.formIsValid = true;
      if (
        this.username === '' ||
        this.password === ''
        // this.password.length < 6
      ) {
        this.formIsValid = false;
        return;
      }

      this.isLoading = true;

      const actionPayload = {
        username: this.username,
        password: this.password,
      };

      if (this.mode === 'login') {
        this.$store.dispatch('login', actionPayload);
      } else {
        this.$store.dispatch('signup', actionPayload);
      }

      const redirectUrl = '/' + (this.$route.query.redirect || 'partners');
      this.$router.replace(redirectUrl);

      this.isLoading = false;
    },
    switchAuthMode() {
      if (this.mode === 'login') {
        this.mode = 'signup';
      } else {
        this.mode = 'login';
      }
    },
    handleError() {
      this.error = null;
    },
  },
};
</script>

<style scoped>
.basic-button {
  background-colour: #ffff;
}

.p-button {
  background-color: $purple-300;
}

form {
  margin: 1rem;
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

.input-block {
  margin: 0.5rem 0;
  /*text-align: center;*/
  /*vertical-align: center;*/
  /*padding: 5rem;*/
  /*display: flex;*/
  /*vertical-align: top;*/
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
</style>