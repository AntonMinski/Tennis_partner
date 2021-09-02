<template>
  <div class="home">
    <div class="container">

      <basic-card>
        <h3 style="text-align: center">Game / training offers:</h3>
      </basic-card>
      <div ref="curBl" v-for="offer in offers" :key="offer.id">
        <basic-card>
        <router-link :to="{ path: '/offers'}" class="question-link">
          <p>
            <basic-icon height="50px" width="20px" icon-name="place"
                    icon-color="#" class="icon-custom">
              <place></place>
            </basic-icon>
            <span>Place:</span> {{ offer.place }}
          </p>
        <p><basic-icon height="15px" width="20px" icon-name="clock"
                       icon-color="#" class="icon-custom">
              <clock></clock>
            </basic-icon>
          <span>Time:</span> {{ offer.time_range }}</p>
        <p><basic-icon height="20px" width="20px" icon-name="level"
             icon-color="#" class="icon-custom">
              <level></level>
            </basic-icon>
          <span>Level NTRP:</span> {{ offer.level }}</p>
        <p><basic-icon height="20px" width="20px" icon-name="calendar"
                       icon-color="#" class="icon-custom">
              <calendar></calendar>
            </basic-icon>
          <span>Date:</span> {{ offer.created_at }}</p>
        <basic-button link :to="detailsLink(offer.id)">
            <basic-icon height="20px" width="20px" icon-name="detailsIcon"
                        class="icon-custom">
              <detailsIcon></detailsIcon>
            </basic-icon>
            View Details</basic-button>
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

import BasicIcon from "../ui/BasicIcon";
import place from "../assets/icons/place";
import clock from "../assets/icons/clock";
import level from "../assets/icons/level";
import calendar from "../assets/icons/calendar";
import detailsIcon from "../assets/icons/detailsIcon";
export default {
  components: {BasicIcon, place, clock, level, calendar, detailsIcon},
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
      this.$store.dispatch('axiosRequest', {endpoint:endpoint})
        .then(response => {
          this.offers.push(...response.data.results);
          this.loadingOffers = false;
          if (response.data.next) {
            this.next = response.data.next;
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
    document.title = "Tennis Partner";
  },
  computed: {

  },
};
</script>

<style scoped>

  .icon-custom {
    height: 25px;
    display: inline-block;
    margin-right: 10px;
    /*width: 18px;*/
    /*color: black;*/
      /*background-color: #81e334;*/
  }

  h3 {
    text-align: center;
  }

.question-author {
  font-weight: bold;
  color: #DC3545;
}

.question-link {
  /*font-weight: bold;*/
  color: black;
}

.question-link span {
   /*font-weight: 505;*/
}

.question-link:hover {
  color: #343A40;
  text-decoration: none;
}


</style>