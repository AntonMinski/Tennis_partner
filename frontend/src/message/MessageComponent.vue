<template>
    <div class="single-answer">
    <p class="text-muted">
      <strong>{{ answer.author }}</strong> &#8901; {{ answer.created_at }}
    </p>
    <p>{{ answer.body }}</p>
    <div v-if="isAnswerAuthor">
      <router-link
        :to="{ name: 'offer_editor', params: { id: answer.id } }"
        class="btn btn-sm btn-outline-secondary mr-1"
        >Edit
      </router-link>
      <button
        class="btn btn-sm btn-outline-danger"
        @click="triggerDeleteAnswer"
        >Delete
      </button>
    </div>
    <div v-else>
      <button
        class="btn btn-sm"
        @click="toggleLike"
        :class="{
          'btn-danger': userLikedAnswer,
          'btn-outline-danger': !userLikedAnswer
          }"
        ><strong>Like [{{ likesCounter }}]</strong>
      </button>
    </div>
    <hr>
  </div>
</template>

<script>
import { apiService } from "../common/api.service";
    export default {
        name: "MessageComponent",
        props: {
        },
        import {api}

    }
</script>

<style scoped>

</style>