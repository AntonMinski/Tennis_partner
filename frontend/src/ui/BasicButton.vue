<template>
    <div class="basic-button-block">
    <button v-if="!link" :class="mode">
        <slot></slot>
    </button>
    <router-link v-else :to="to" :class="mode">
        <slot></slot>
    </router-link>
        </div>
</template>

<script>
    export default {
        props: {
            link: {
                type: Boolean,
                required: false,
                default: false,
            },
            to: {
                type: String,
                required: false,
                default: '/',
            },
            mode: {
                type: String,
                required: false,
                default: null
            },
        },
    };
</script>

<style scoped>
.basic-button-block{
    display: block;
    margin: 0.75rem 0;
}

button,
a {
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

a:hover,
a:active,
button:hover,
button:active {
  background-color: #8ace60;
  border-color: #adce60;
    color: white;
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

.flat:hover,
.flat:active,
.outline:hover,
.outline:active {
  background-color: #8ace60;
    border: #8ace60;
}
</style>