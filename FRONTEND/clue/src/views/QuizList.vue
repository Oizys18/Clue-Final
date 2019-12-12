<template>
  <div class="quizlist">
    <div class="pt-2">
      <vs-row vs-justify="center">
        <vs-row vs-justify="center">
          <vs-select
            width="300px"
            placeholder="Pick a Genre"
            multiple
            autocomplete
            @input="ChangeList()"
            label-placeholder="Autocomplete"
            class="selectGenre"
            v-model="pickedGenres"
          >
            <vs-select-item
              :key="index"
              :value="item.content"
              :text="item.content"
              v-for="(item, index) in genres"
            />
          </vs-select>
        </vs-row>
      </vs-row>
      <div :key="quizSetKey">
        <QuizListItem v-for="movie in movies" :key="movie.id" :movie="movie" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import QuizListItem from "@/components/QuizListItem.vue";

export default {
  name: "QuizList",
  components: {
    QuizListItem
  },
  data() {
    return {
      select1Normal: "",
      quizSetKey: 0,
      pickedGenres: [],
      serialGenres: "+",
      genres: [],
      movies: {},
      BASE_URL: "https://final-be.herokuapp.com"
    };
  },
  methods: {
    getMovies() {
      const token = this.$session.get("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios
        .get(
          `${this.BASE_URL}/api/v1/movies/pick_n/5/${this.serialGenres}/`,
          options
        )
        .then(res => {
          this.movies = res.data;
        });
    },
    getGenres() {
      const token = this.$session.get("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios.get(`${this.BASE_URL}/api/v1/movies/genres/`, options).then(res => {
        this.genres = res.data;
      });
    },
    ChangeList() {
      if (this.pickedGenres.length === 0) {
        this.getMovies();
      } else {
        this.quizSetKey += 1;
        for (let idx in this.pickedGenres) {
          this.serialGenres += `${this.pickedGenres[idx]}+`;
        }
        const token = this.$session.get("jwt");
        const options = {
          headers: {
            Authorization: "JWT " + token
          }
        };
        axios
          .get(
            `${this.BASE_URL}/api/v1/movies/pick_n/5/${this.serialGenres}/`,
            options
          )
          .then(res => {
            this.movies = res.data;
          });
        this.quizSetKey += 1;
        this.serialGenres = "+";
      }
    }
  },
  beforeMount() {
    this.getMovies();
    this.getGenres();
  }
};
</script>

<style scoped>
.quizlist {
  width: 100%;
  height:100%;
  color: black;
  background: linear-gradient(-45deg, #3e5151, #decba4);
  background-size: 600% 500%;
  animation: gradientBG 8s ease infinite;
}

@keyframes gradientBG {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
</style>
