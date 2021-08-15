<template>
  <div class="home">
    <div class="container">
      <basic-card><h3>Game / training offers:</h3></basic-card>
      <div ref="curBl" v-for="offer in offers" :key="offer.id">
        <basic-card>
        <router-link :to="{ path: '/offers'}"

        class="question-link">
        <p>Posted by: {{ offer.author }}</p>
        <p>Place: {{ offer.place }}</p>
        <p>Time: {{ offer.time_range }}</p>
        <p>Level NTRP: {{ offer.level }}</p>
        <p>Date: {{ offer.created_at }}</p>
        <basic-button link :to="detailsLink(offer.id)">View Details</basic-button>
          </router-link>
          </basic-card>
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

export default {
  data() {
    return {
      offers: [],
      next: null,
      loadingOffers: false,
      ckey: '',
    };
  },
  methods: {
    getOffers() {
      let endpoint = "api/offers/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingOffers = true;
      this.axiosService(endpoint)
        .then(data => {
          this.offers.push(...data.results);
          this.loadingOffers = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        });
      this.loadingOffers = false;
    },
    detailsLink(id) {
      return this.$route.path + '/' + id
    },
  },
  created() {
    this.getOffers();
    // this.makeLink();
    document.title = "Tennis Partner";
  },
  computed: {
    // offerDetailsLink() {
    //   return this.$route.path + '/' + this.$refs.curBl.key
    // },
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