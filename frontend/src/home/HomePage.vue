<template>
  <div class="home">
    <div class="container">
      <div v-for="offer in offers" :key="offer.id">
        <p class="mb-0">
          Posted by:
          <span>{{ offer.author }} </span>
        </p>
        <h4>OfferPage details:</h4>
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
      <div class="my-4" >
        <p v-if="loadingOffers">...loading...</p>
        <button v-if="next" @click="getOffers">Load more</button>
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
      next: null,
      loadingOffers: false,
    };
  },
  methods: {

    getOffers() {
      let endpoint = "api/offers/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingOffers = true;
      apiService(endpoint).then((data) => {
        this.offers.push(...data.results);
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
      this.loadingOffers = false;
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