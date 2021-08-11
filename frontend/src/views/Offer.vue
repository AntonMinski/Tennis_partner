<template>
    <div class="single-question mt-2">
    <div v-if="offer" class="container">
      <h1>Offer details:</h1>
        <p>{{ offer.place }}</p>
        <p>{{ offer.time_range }}</p>
        <p>{{ offer.level }}</p>
        <p>{{ offer.game_type }}</p>
        <p>{{ offer.details }}</p>
        <p>{{ offer.created_at }}</p>
<!--      <QuestionActions-->
<!--        v-if="isQuestionAuthor"-->
<!--        :slug="question.slug"-->
<!--      />-->
<!--      <p class="mb-0">Posted by:-->
<!--        <span class="author-name">{{ question.author }}</span>-->
<!--      </p>-->
<!--      <p>{{ question.created_at }}</p>-->
<!--      <hr>-->
<!--      <div v-if="userHasAnswered">-->
<!--        <p class="answer-added">You've written an answer!</p>-->
<!--      </div>-->
<!--      <div v-else-if="showForm">-->
<!--        <form class="card" @submit.prevent="onSubmit">-->
<!--          <div class="card-header px-3">-->
<!--            Answer the Question-->
<!--          </div>-->
<!--          <div class="card-block">-->
<!--            <textarea-->
<!--              v-model="newAnswerBody"-->
<!--              class="form-control"-->
<!--              placeholder="Share Your Knowledge!"-->
<!--              rows="5"-->
<!--            ></textarea>-->
<!--          </div>-->
<!--          <div class="card-footer px-3">-->
<!--            <button type="submit" class="btn btn-sm btn-success">Submit Your Answer</button>-->
<!--          </div>-->
<!--        </form>-->
<!--        <p v-if="error" class="error mt-2">{{ error }}</p>-->
<!--      </div>-->
<!--      <div v-else>-->
<!--        <button-->
<!--          class="btn btn-sm btn-success"-->
<!--          @click="showForm = true"-->
<!--          >Answer the Question-->
<!--        </button>-->
<!--      </div>-->
<!--      <hr>-->
<!--    </div>-->
<!--    <div v-else>-->
<!--      <h1 class="error text-center">404 - Question Not Found</h1>-->
<!--    </div>-->
<!--    <div v-if="question" class="container">-->
<!--      <AnswerComponent-->
<!--        v-for="answer in answers"-->
<!--        :answer="answer"-->
<!--        :requestUser="requestUser"-->
<!--        :key="answer.id"-->
<!--        @delete-answer="deleteAnswer"-->
<!--      />-->
<!--      <div class="my-4">-->
<!--        <p v-show="loadingAnswers">...loading...</p>-->
<!--        <button-->
<!--          v-show="next"-->
<!--          @click="getQuestionAnswers"-->
<!--          class="btn btn-sm btn-outline-success"-->
<!--          >Load More-->
<!--        </button>-->
<!--      </div>-->
    </div>
  </div>
</template>

<script>
  import { apiService } from "../common/api.service";
    export default {
        name: "Offer",
      props: {
        slug: {
          type: String,
          required: true
        }
      },
      data() {
          return {
            offer: {},
          };
      },
      methods: {
          setPageTitle(title) {
              document.title = title;
          },
          getOfferData() {
              let endpoint = `/api/offers/${this.slug}`;
              apiService(endpoint)
                  .then(data => {
                      this.offer = data;
                  })
          },
      },
      created() {
          this.getOfferData();
          this.setPageTitle('Offer details:');
      }
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