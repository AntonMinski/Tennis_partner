<template>
    <li>
        <h3>{{ fullName }}</h3>
        <h4>{{ skillLevel }}/6 - NTRP</h4>
        <div>
            <basic-badge v-for="style in sportStyles" :key="style" :type="style"
                         :title="style"></basic-badge>
        </div>
        <div class="actions">
            <basic-button mode="outline" link :to="partnerContactLink">Contact</basic-button>
            <basic-button link :to="partnerDetailsLink">View Details</basic-button>
        </div>
    </li>
</template>

<script>
    import BasicButton from "../ui/BasicButton";
    import BasicBadge from "../ui/BasicBadge";
    export default {
        components: {BasicBadge, BasicButton},
        props: ['id', 'firstName', 'lastName', 'sportStyles', 'skillLevel', ],
        computed: {
            fullName() {
                return this.firstName + " " + this.lastName;
            },
            partnerContactLink() {
                return this.$route.path + '/' + this.id + '/contact'; // this.$route.path - текущий адрес маршрута, в котором находимся
            },
            partnerDetailsLink () {
                return this.$route.path + '/' + this.id;
            },
        },
    };
</script>

<style scoped>
li {
  margin: 1rem 0;
  border: 1px solid #424242;
  border-radius: 12px;
  padding: 1rem;
}

h3 {
  font-size: 1.5rem;
}

h3,
h4 {
  margin: 0.5rem 0;
}

div {
  margin: 0.5rem 0;
}

.actions {
  display: flex;
  justify-content: flex-end;
}
</style>