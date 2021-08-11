/* eslint-disable */

<template>
  <div class="container mt-2">
    <h1 class="mb-3">Create an offer</h1>
    <form @submit.prevent="submitOffer">
      <input v-model="place" class="form-control" placeholder="place" />
      <input v-model="time_range" class="form-control" placeholder="time" />
      <input v-model="level" class="form-control" placeholder="level" />
      <input v-model="game_type" class="form-control" placeholder="game_type" />
      <textarea
        v-model="details"
        class="form-control"
        placeholder="Describe your game / training offer"
        rows="3"
      ></textarea>
      <br />
      <button type="submit" class="btn btn-success">Publish</button>
    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "../common/api.service";
export default {
  name: "OfferEditor",
  data() {
    return {
      place: "",
      time_range: "",
      level: null,
      game_type: null,
      details: null,
      error: null,
    };
  },
  created() {
    document.title = "Editor - Tennis partner";
  },
  methods: {
    submitOffer() {
      let endpoint = "/api/offers/";
      let method = "POST";
      const data = {
        place: this.place,
        time_range: this.time_range,
        level: this.level,
        game_type: this.game_type,
        details: this.details,
      };
      apiService(endpoint, method, data)
        .then((offer_data) => {
          console.log(offer_data);
          this.$router.push({
            name: "offer",
            params: { slug: offer_data.id },
          });
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped></style>
