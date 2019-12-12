<template>
  <div class="pt-2">
    <vs-row vs-justify="center">
      <vs-col
        type="flex"
        vs-justify="center"
        vs-align="center"
        vs-w="4.5"
        vs-xs="9"
        vs-lg="7"
      >
        <a @click="solve()">
          <div class="quizcard2 shadow rounded bg-white p-4">
            <h3>Quiz #{{ movie.id }}</h3>
            <vs-chip
              class="badge-color2"
              v-for="genre in movie.movie_genres"
              :key="genre.id"
            >
              <vs-avatar class="badge-avatar-color2" text="G" />{{
                genre.content
              }}
            </vs-chip>
            <vs-divider />
            <div>
              <span
                v-for="keyword in movie.movie_keywords.slice(0, 10)"
                :key="keyword.id"
                ><vs-chip class="badge-keyword">
                  {{ keyword.content }}
                </vs-chip></span
              >
            </div>
            <vs-row></vs-row>
          </div>
        </a>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
import router from "@/router";
export default {
  name: "QuizListItem",
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  methods: {
    solve() {
      router.push(`/quiz?movie_pk=${this.movie.id}`);
    }
  }
};
</script>

<style scoped>
.quizcard2:hover {
  background-color: #a4ad80 !important;
}
.badge-color2 {
  background-color: #152218 !important;
  color: #cbe9c7 !important;
  font-weight: bold;
}
.badge-avatar-color2 {
  background-color: #2d4b2d !important;
  color: #6e0606 !important;
}
.badge-keyword {
  background-color: #b17753 !important;
  color: #050501 !important;
  font-weight: bold;
}
</style>
