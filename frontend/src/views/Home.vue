<template>
  <div class="home">
    <div class="container">
      <div v-for="offer in offers" :key="offer.id">
        <p class="mb-0">
          Posted by:
          <span>{{ offer.author }} </span>
        </p>
        <h4>Offer details:</h4>
        <router-link :to="{ name: 'offer', params: {slug: offer.id} }"
        class="question-link">
        <p>{{ offer.place }}</p>
        <p>{{ offer.time_range }}</p>
        <p>{{ offer.level }}</p>
        <p>{{ offer.game_type }}</p>
        <p>{{ offer.created_at }}</p>
          </router-link>
<!--        <p>{{ offer.details }}</p>-->
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import { apiService } from "../common/api.service";

export default {
  name: "Home",
  components: {},
  data() {
    return {
      offers: [],
    };
  },
  methods: {

    getOffers() {
      let endpoint = "api/offers/";
      apiService(endpoint).then((data) => {
        this.offers.push(...data.results);
      });
    },
  },
  created() {
    this.getOffers();
    console.log(this.offers);
    document.title = "Tennis Partner";
  },
};
</script>

<style scoped>
.question-author {
  font-weight: bold;
  color: #DC3545;
}

.question-link {
  font-weight: bold;
  color: black;
}

.question-link:hover {
  color: #343A40;
  text-decoration: none;
}
</style>