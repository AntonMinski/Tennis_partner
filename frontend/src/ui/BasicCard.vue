<template>
<!--    <div class="outer_card">-->
    <div class="basic-card">
    <slot></slot>
        </div>
<!--        </div>-->
</template>

<script>
    export default {
        name: "BasicCard"
    }
</script>

<style v-slot>
span {
   font-weight: 600;
}

    /*.outer_card {*/
    /*    padding: 0;*/
    /*    max-width: 40rem;*/
    /*    border-radius: 12px;*/
    /*    box-shadow: -20px -20px 20px rgba(255, 255, 255, 0.4);*/
    /*}*/

.basic-card {
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.26);
    padding: 1rem;
    margin: 2rem auto;
    max-width: 40rem;
    color: #575757;
    /*background-color: #f8f8f8;*/
    /*background: linear-gradient(166deg, rgba(255,255,255,1) 0%, rgba(250,255,255,1) 17%, rgba(250,250,250,1) 39%, rgba(251,251,251,1) 81%, rgba(255,255,255,1) 100%);*/
}
</style>