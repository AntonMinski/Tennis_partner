<template>
    <div class="card">
    <slot></slot>
        </div>
</template>

<script>
    export default {
        name: "BasicCard"
    }
</script>

<style scoped>
.card {
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.26);
    padding: 1rem;
    margin: 2rem auto;
    max-width: 40rem;
    color: #575757;
    background-color: #f8f8f8;
}
</style>