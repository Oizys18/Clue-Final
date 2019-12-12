<template>
  <div>
    <!-- <div class="quiz-reveal-bg"></div> -->
    <vs-tabs color="#515244" alignment="center">
      <vs-tab label="Info">
        <div>
          <vs-row>
            <vs-col vs-w="0" vs-xs="12">
              <h2 class="mt-3 font-noto font-weight-bold">{{ movie.title }}</h2>
              <div class="mt-3 mb-2" style="height: 28px">
                <vs-chip class="badge-color0">
                  <vs-avatar text="Y" class="badge-avatar-color3" />
                  {{ movie.year }}
                </vs-chip>
                <vs-chip class="badge-color0">
                  <vs-avatar text="R" class="badge-avatar-color4" />
                  {{ movie.rating }}
                </vs-chip>
                <vs-chip class="badge-color0" v-for="genre in movie.movie_genres" :key="genre.id">
                  <vs-avatar text="G" class="badge-avatar-color2" />
                  {{ genre.content }}
                </vs-chip>
              </div>
              <vs-row></vs-row>
              <div class="mt-3">
                <vs-divider position="left">
                  <span class="font-source font-weight-bold">plot</span>
                </vs-divider>
                <p class="font-source ml-3">{{ movie.plot }}</p>
              </div>
            </vs-col>
            <vs-col vs-w="6" vs-xs="12">
              <div class="shadow">
                <img
                  class="img-fluid"
                  style="width: 100%"
                  :src="movie.poster_url"
                  :alt="movie.title"
                />
              </div>
            </vs-col>
            <vs-col vs-w="0" vs-xs="12">
              <div class="mt-3">
                <vs-divider position="left">
                  <span class="font-source font-weight-bold">director</span>
                </vs-divider>
                <p class="font-source ml-3">
                  <span
                    v-for="director in movie.movie_directors"
                    :key="director.id"
                  >{{ director.name }}</span>
                </p>
              </div>
              <div class="mt-3">
                <vs-divider position="left">
                  <span class="font-source font-weight-bold">cast</span>
                </vs-divider>
                <p class="font-source ml-3">
                  <span v-for="person in castList" :key="person.id">{{ person.name }} .</span>
                </p>
              </div>
            </vs-col>
            <vs-col vs-offset="0.5" vs-w="4" vs-xs="0">
              <h2 class="mt-3 font-noto font-weight-bold">{{ movie.title }}</h2>
              <div class="mt-3 mb-2" style="height: 28px">
                <vs-chip class="badge-color0">
                  <vs-avatar text="Y" class="badge-avatar-color3" />
                  {{ movie.year }}
                </vs-chip>
                <vs-chip class="badge-color0">
                  <vs-avatar text="R" class="badge-avatar-color4" />
                  {{ movie.rating }}
                </vs-chip>
                <vs-chip class="badge-color0" v-for="genre in movie.movie_genres" :key="genre.id">
                  <vs-avatar text="G" class="badge-avatar-color2" />
                  {{ genre.content }}
                </vs-chip>
              </div>
              <vs-row></vs-row>
              <div class="mt-3">
                <vs-divider position="left">
                  <span class="font-source font-weight-bold">plot</span>
                </vs-divider>
                <p class="font-source ml-3">{{ movie.plot }}</p>
              </div>
              <div class="mt-3">
                <vs-divider position="left">
                  <span class="font-source font-weight-bold">director</span>
                </vs-divider>
                <p class="font-source ml-3">
                  <span
                    v-for="director in movie.movie_directors"
                    :key="director.id"
                  >{{ director.name }}</span>
                </p>
              </div>
              <div class="mt-3">
                <vs-divider position="left">
                  <span class="font-source font-weight-bold">cast</span>
                </vs-divider>
                <p class="font-source ml-3">
                  <span v-for="person in castList" :key="person.id">{{ person.name }} .</span>
                </p>
              </div>
            </vs-col>
          </vs-row>
        </div>
      </vs-tab>
      <vs-tab label="Reviews">
        <div>
          <vs-row vs-type="flex" vs-justify="center">
            <vs-col>
              <form @submit.prevent="createReview" class="d-flex justify-content-center">
                <vs-input size="small" v-model="reviewText"></vs-input>
                <vs-button size="small" @click="createReview">submit</vs-button>
              </form>
            </vs-col>
          </vs-row>
          <vs-row vs-type="flex" vs-justify="center">
            <vs-col vs-w="10" vs-xs="12">
              <div :key="reviewKey">
                <div
                  v-for="review in movie.review_set"
                  :key="review.id"
                  class="d-flex justify-content-between align-item-center mx-2 my-2"
                >
                  <div class="align-items-center">
                    <vs-chip class="m-0 mr-3 badge-color0">
                      {{ review.user.username }}
                      <small
                        class="ml-2"
                      >{{ review.created_at.slice(0,10)}}</small>
                    </vs-chip>
                  </div>
                  <span class="lead">
                    <em>" {{ review.content }} "</em>
                  </span>
                  <div>
                    <button
                      class="badge badge-pill badge-danger"
                      @click="deleteReview(review.id)"
                    >delete</button>
                  </div>
                </div>
              </div>
            </vs-col>
          </vs-row>
        </div>
      </vs-tab>
      <!-- <vs-tab label="Trailer">
        <div class="col-12">
          <iframe
            style="height:500px;width:inherit"
            src="https://www.youtube.com/embed/3Ro9ebQxEOY"
            frameborder="0"
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          ></iframe>
        </div>
      </vs-tab>-->
    </vs-tabs>
    <div class="like">
    <vs-chip color="danger">
      <vs-avatar color="warning" text="♥" @click="likeMovie" />like
    </vs-chip>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import jwtDecode from "jwt-decode";

export default {
  name: "QuizReveal",
  props: {
    movie: {
      type: Object,
      required: true
    },
    castList: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      state: 0,
      userId: "",
      isSuperuser: false,
      // review
      reviewKey: 0,
      reviewText: ""
      // review end
    };
  },
  methods: {
    createReview() {
      const token = this.$session.get("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      const data = {
        content: this.reviewText,
        movie_id: this.movie.id,
        user_id: jwtDecode(token).user_id
      };
      console.log(data);

      axios
        .post(
          `https://final-be.herokuapp.com/api/v1/movies/${this.movie.id}/reviews/`,
          { content: this.reviewText },
          options
        )
        .then(res => {
          console.log(res);
          this.reviewText = "";
          this.reviewUpdate();
        })
        .catch(err => {
          console.log(err);
        });
    },
    deleteReview(reviewId) {
      console.log(reviewId);
      const token = this.$session.get("jwt");
      console.log(token);
      const options = {
        headers: {
          Authorization: "JWT " + token
        },
        data: {
          review_id: reviewId
        }
      };
      axios
        .delete(
          `https://final-be.herokuapp.com/api/v1/movies/${this.movie.id}/reviews/`,
          options
        )
        .then(res => {
          console.log(res);
          this.reviewUpdate();
          this.reviewKey++;
        });

      // Observe the data keyword this time. Very important
      // payload is the request body
      // Do something
    },
    getUserId() {
      const token = this.$session.get("jwt");
      this.userId = jwtDecode(token).user_id;
      this.isSuperuser = jwtDecode(token).is_superuser;
      console.log(jwtDecode(token));
      console.log("current usr", this.userId, this.isSuperuser);
    },
    reviewUpdate() {
      const token = this.$session.get("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios
        .get(
          `https://final-be.herokuapp.com/api/v1/movies/${this.movie.id}/reviews/`,
          options
        )
        .then(res => {
          this.movie.review_set = res.data;
        });
    },
    likeMovie() {
      console.log("like");
      const token = this.$session.get("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      const data = {};
      axios
        .post(
          `https://final-be.herokuapp.com/api/v1/movies/${this.movie.id}/like/`,
          data,
          options
        )
        .then(res => {
          console.log(res);
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  mounted() {
    console.log(this.movie.review_set);
    this.getUserId();
  }
};
</script>

<style scoped>
.badge-avatar-color2 {
  background-color: #2d4b2d !important;
  color: #6e0606 !important;
}
.badge-avatar-color3 {
  background-color: #ffb516 !important;
  color: black !important;
  cursor: initial !important;
}
.badge-avatar-color4 {
  background-color: #ff4810 !important;
  color: black !important;
  cursor: initial !important;
}
.badge-color0 {
  font-weight: bold;
}
.info-plot {
  line-height: 1.3;
}
.quiz-reveal-bg {
  background-color: white !important;
  position: fixed;
  height: 100%;
  width: inherit;
}
.like {
  position: fixed;
  bottom: 5px;
  left: 5px;
}
</style>
