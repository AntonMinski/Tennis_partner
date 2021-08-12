<template>
    <section>
        <basic-card>
            <h2>Register as player</h2>
            <partner-form @save-data="saveData"></partner-form>
        </basic-card>
    </section>
</template>

<script>
    import PartnerForm from "./PartnerForm";

    export default {
        components: {PartnerForm},

        methods: {
            saveData(formData) {
                this.$store.dispatch('partners/registerPartner', formData)
                this.$router.replace('/partners')
            },
        },
    };
</script>

<style scoped>

</style>