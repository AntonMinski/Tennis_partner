<template>

        <div class="single-question mt-2">
            <basic-card><div><h4>Offer details:</h4></div></basic-card>
            <basic-card>
            <div v-if="offer" class="container"
            >
                <div><h4></h4></div>
                <p>Posted by: {{ offer.author }}</p>
                <p>Place: {{ offer.place }}</p>
                <p>Time: {{ offer.time_range }}</p>
                <p>Level NTRP: {{ offer.level }}</p>
                <p>Game type: {{ offer.game_type }}</p>
                <p>Game details: {{ offer.details }}</p>
                <p>Date: {{ offer.created_at }}</p>

            </div>
                </basic-card>
            <basic-card>

        <basic-button link :to="contactLink">Contact partner</basic-button>
        <basic-button>Book a court</basic-button>
        <basic-button>View partner profile</basic-button>
        <basic-button>contact by messenger</basic-button>
        <router-view :message-receiver="offerAuthor"
        ></router-view>
    </basic-card>
        </div>



</template>

<script>
    import ContactPartner from "../message/ContactPartner";
    export default {
        name: "Offer",
        components: {ContactPartner,},
        props: {
        id: {
          type: String,
          required: true
        },
      },
      data() {
          return {
            offer: {},
            offerAuthor: '',
          };
      },
      methods: {
          setPageTitle(title) {
              document.title = title;
          },
          getOfferData() {
              let endpoint = `/api/offers/${this.id}/`;
              this.$store.dispatch('axiosRequest', endpoint)
                  .then(data => {
                      this.offer = data;
                      this.offerAuthor = data.author;
                  })
          },
      },
      created() {
          this.getOfferData();
          this.setPageTitle('Offer details:');
      },
        computed: {
          contactLink() {
             return '/offers/' + this.id + '/contact';
          },
        },
    };
</script>

<style scoped>
.author-name {
  font-weight: bold;
  color: #DC3545;
}

.answer-added {
  font-weight: bold;
  color: green;
}

.error {
  font-weight: bold;
  color: red;
}
</style>