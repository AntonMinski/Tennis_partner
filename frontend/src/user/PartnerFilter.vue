<template>
    <basic-card>
        <h2>Find your Partner by style:</h2>
        <span class="filter-options">
        <input type="checkbox" id="football" checked @change="setFilter"
               class="custom-checkbox"/>
        <label for="football">Football</label>
        </span>
        <span class="filter-options">
        <input type="checkbox" id="tennis" checked @change="setFilter"
               class="custom-checkbox"/>
        <label for="tennis">Tennis</label>
        </span>
        <span class="filter-options">
        <input type="checkbox" id="bike" checked @change="setFilter"
               class="custom-checkbox"/>
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

    .custom-checkbox {
  position: absolute;
  z-index: -1;
  opacity: 0;
}
    .custom-checkbox+label {
  display: inline-flex;
  align-items: center;
  user-select: none;
}
.custom-checkbox+label::before {
  content: '';
  display: inline-block;
  width: 1.2em;
  height: 1.2em;
  flex-shrink: 0;
  flex-grow: 0;
  border: 1px solid var(--bg-border);
  border-radius: 0.25em;
  margin-right: 0.5em;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: 50% 50%;
}

.custom-checkbox:checked+label::before {
  border-color: var(--secondary);
  background-color: var(--primary);
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%23fff' d='M6.564.75l-3.59 3.612-1.538-1.55L0 4.26 2.974 7.25 8 2.193z'/%3e%3c/svg%3e");
}

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