<template>
    <div>
        <section>
            <basic-card>
                <h2>{{ fullName }}</h2>
                <h3>{{ skills }}/6 - NTRP</h3>
            </basic-card>
        </section>
        <section>
            <basic-card>
                <header>
                    <h2>Want to play together? Lets go now!</h2>
                    <basic-button link :to="contactLink">Contact</basic-button>
                </header>
                <router-view></router-view>
            </basic-card>
        </section>
        <section>
            <basic-card>
                <basic-button v-for="style in sportStyles" :key="style"
                              :type="style" :title="style">{{ style }}
                </basic-button>
                <p>{{ description }}</p>
            </basic-card>
        </section>
    </div>
</template>

<script>
    import BasicButton from "../ui/BasicButton";
    // import BasicBadge from "../components/ui/BasicBadge";
    export default {
        name: "PartnerDetails",
        components: {BasicButton},
        props: ['id'],
        data() {
            return {
                selectedPatner: null,
            };
        },
        computed: {
            fullName() {
                return this.selectedPatner.firstName + ' '
                    + this.selectedPatner.lastName;
            },
            contactLink() {
                return '/partners/' + this.id + '/contact';
            },
            sportStyles() {
                return this.selectedPatner.sportStyles;
            },
            skills() {
                return this.selectedPatner.skillLevel;
            },
            description() {
                return this.selectedPatner.description;
            },
        },
        created() {
            this.selectedPatner =
                this.$store.getters['partners/partners'].find(partner => partner.id === this.id);
        }
    }
</script>

<style scoped>

</style>