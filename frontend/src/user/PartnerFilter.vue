<template>
    <basic-card>
        <h2>Find your Partner by style:</h2>
        <span class="filter-option">
        <input type="checkbox" id="football" @change="setFilter" />
            <label for="football">Football</label>
        </span>
           <span class="filter-options">
        <input type="checkbox" id="tennis" checked @change="setFilter" />
            <label for="tennis">Tennis</label>
        </span>
           <span class="filter-options">
        <input type="checkbox" id="bike" checked @change="setFilter" />
            <label for="bike">Bike</label>
        </span>
    </basic-card>
</template>

<script>
    export default {
        emits: ['change-filter'],
        data() {
            return {
                filters: {
                    football: false,
                    tennis: true,
                    bike: true,
                },
            };
          },
        methods: {
            setFilter(event) {
                const inputId = event.target.id;
                const isActive = event.target.checked;
                const updatedFilters = {
                    ...this.filters,
                    [inputId]: isActive
                };
                this.filters = updatedFilters;
                this.$emit('change-filter', updatedFilters);
            },
        },
    }
</script>

<style scoped>
h2 {
  margin: 0.5rem 0;
}

.filter-option {
  margin-right: 1rem;
}

.filter-option label,
.filter-option input {
  vertical-align: middle;
}

.filter-option label {
  margin-left: 0.25rem;
}

.filter-option.active label {
  font-weight: bold;
}
</style>