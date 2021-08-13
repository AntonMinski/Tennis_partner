<template>

        <div class="single-question mt-2">
            <basic-card><div><h4>Offer details:</h4></div></basic-card>
            <basic-card>
            <div v-if="offer" class="container">
                <div><h4></h4></div>
                <p>Posted by: {{ offer.author }}</p>
                <p>Place: {{ offer.place }}</p>
                <p>Time: {{ offer.time_range }}</p>
                <p>Level NTRP: {{ offer.level }}</p>
                <p>Game type: {{ offer.game_type }}</p>
                <p>Game details: {{ offer.details }}</p>
                <p>Date: {{ offer.created_at }}</p>

                <div>
                <!--      <QuestionActions-->
                <!--        v-if="isQuestionAuthor"-->
                <!--        :id="question.id"-->
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
                </basic-card>
            <basic-card>
        <basic-button link :to="contactLink">Contact partner</basic-button>
        <basic-button>Book a court</basic-button>
        <basic-button>View partner profile</basic-button>
        <basic-button>contact by messenger</basic-button>
        <router-view></router-view>
    </basic-card>
        </div>



</template>

<script>
    import {apiService, axiosService} from "../common/api.service";
  import BasicCard from "../ui/BasicCard";
  import BasicButton from "../ui/BasicButton";
    export default {
        name: "Offer",
        components: {BasicButton, BasicCard},
        props: {
        id: {
          type: String,
          required: true
        },
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
              let endpoint = `/api/offers/${this.id}/`;
              // apiService(endpoint)
              axiosService(endpoint)
                  .then(data => {
                      this.offer = data;
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