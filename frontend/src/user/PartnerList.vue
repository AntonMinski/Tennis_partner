<template>
    <div>
        <basic-dialog :show="!!error" title="We received an error..."
                      @close="handleError">
            <p>{{ error }}</p>
        </basic-dialog>
        <section>
            <partner-filter @change-filter="setFilters"></partner-filter>
        </section>
        <section>
            <basic-card>
                <div class="controls">
                    <basic-button mode="outline" @click="loadPartners(true)">
                        Refresh
                    </basic-button>
                    <basic-button link to="/auth?redirect=register" v-if="isLoggedIn">
                        Register as stuff</basic-button>
                    <basic-button link to="/register" v-if="isLoggedIn">
                        Register as Player
                    </basic-button>
                </div>
                <div v-if="isLoading">
                    <loading-spinner></loading-spinner>
                </div>
                <ul v-else-if="hasPartners">
                    <partner-item v-for="partner in filteredPartners"
                                  :id="partner.id"
                                  :key="partner.id"
                                  :first-name="partner.firstName"
                                  :last-name="partner.lastName"
                                  :skill-level="partner.skillLevel"
                                  :sport-styles="partner.sportStyles"
                    ></partner-item>
                </ul>
                <h3 v-else>No partners found.</h3>
            </basic-card>
        </section>
    </div>
</template>

<script>
    import PartnerItem from "./PartnerItem";
    import BasicButton from "../ui/BasicButton";
    import PartnerFilter from "./PartnerFilter";
    import BasicDialog from "../ui/BasicDialog";

    export default {
        components: {BasicDialog, BasicButton, PartnerItem, PartnerFilter},
        data() {
            return {
                isLoading: false,
                error: null,
                activeFilters: {
                    // strange bug: if at start all 3 would be "true", it would
                    // not work; Now all 3 filters work as should
                    football: false,
                    tennis: true,
                    bike: true,
                },
            };
        },
        computed: {
            filteredPartners() {
                const partners = this.$store.getters['partners/partners'];
                console.log(partners)
                return partners.filter(partner => {
                    if (this.activeFilters.football &&
                        partner.sportStyles.includes('football')) {
                        console.log('football', partner.id);
                        return true;

                    }
                    if (this.activeFilters.tennis &&
                        partner.sportStyles.includes('tennis')) {
                        return true;
                    }
                    if (this.activeFilters.bike &&
                        partner.sportStyles.includes('bike')) {
                        return true;
                    }
                    return false;

                });
            },
            hasPartners() {
                return !this.isLoading && this.$store.getters['partners/hasPartners'];
            },
            isRegistered() {
                return this.$store.getters['partners/isRegistered'];
            },
            isLoggedIn() {
                return this.$store.getters.isAuthenticated;
            }

        },
        created() {
            this.loadPartners();
        },
        methods: {
            setFilters(updatedFilters) {
                this.activeFilters = updatedFilters;
            },
            async loadPartners(refresh = false) {
                this.isLoading = true;
                try {
                    await this.$store.dispatch('partners/loadPartners', {forceRefresh: refresh});

                } catch (error) {
                    this.error = error.message || 'Uknown error';
                }
                this.isLoading = false;
            },
            handleError() {
                this.error = null;
            },
        },
    };
</script>

<style scoped>
    ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }

    .controls {
        display: flex;
        justify-content: space-between;
    }
</style>