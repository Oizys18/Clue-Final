<template>
  <div>
    <vs-row vs-justify="center" vs-align="center">
      <vs-col vs-w="8" vs-xs="12" vs-sm="10">
        <QuizItem
          :class="fadeIn"
          class="shadow rounded bg-white my-4 mx-5 p-4"
          :movie="movie"
          :hiddenItems="hiddenItems"
          :keywordsList="keywordsList"
          :plotList="plotList"
          :genreList="genreList"
          @onRevealKey="revealKey"
          @onRevealAll="revealAll"
          @onRevealPlot="revealPlot"
        />
      </vs-col>
    </vs-row>
    <vs-row vs-justify="center" vs-align="center">
      <vs-col vs-w="10" vs-xs="12" vs-sm="11" vs-lg="9">
        <QuizReveal v-if="!hiddenItems.hidden" :movie="movie" :castList="castList" />
      </vs-col>
    </vs-row>

  </div>
  <!-- </div> -->
</template>

<script>
import axios from "axios";
import router from "@/router";
import jwtDecode from "jwt-decode";
import QuizItem from "@/components/QuizItem.vue";
import QuizReveal from "@/components/QuizReveal.vue";

export default {
  name: "Quiz",
  components: {
    QuizItem,
    QuizReveal
  },
  data() {
    return {
      username: "",
      userinfo: {},
      movie: {},
      BASE_URL: "https://final-be.herokuapp.com",
      keywordsList: [],
      plotList: [],
      genreList: [],
      castList: [],
      hiddenItems: {},
      fadeIn: ""
    };
  },
  methods: {
    getSpecificMovie(q) {
      const token = this.$session.get("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios
        .get(`${this.BASE_URL}/api/v1/movies/${q}`, options)
        .then(res => {
          console.log(res);
          this.movie = res.data;
          this.getList(this.movie);
          this.makeHiddenItems(this.movie);
          this.revealifSeenmovie();
        })
        .catch(err => {
          console.log(err.response);
          if (err.response.status === 401) {
            router.push("/login").catch(err => {
              err;
            });
          }
        });
    },
    getMovies() {
      // console.log(this.$route.query.movie_pk)
      const token = this.$session.get("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios
        .get(`${this.BASE_URL}/api/v1/movies/pick_n/`, options)
        .then(res => {
          this.movie = res.data[0];
          this.getList(this.movie);
          this.makeHiddenItems(this.movie);
          this.revealifSeenmovie();
          console.log(this.movie.movie_seen_users);
        })
        .catch(err => {
          console.log(err.response);
          if (err.response.status === 401) {
            router.push("/login").catch(err => {
              err;
            });
          }
        });
    },
    revealKey(keyword) {
      const index = this.keywordsList.indexOf(keyword);
      this.keywordsList[index].hidden = 0;
    },
    revealAll() {
      this.seenMovies();
      this.getCast();
      this.fadeIn = "quizitem";
      this.hiddenItems.hidden = 0;
      this.keywordsList = this.keywordsList.map(item => {
        item.hidden = 0;
        return item;
      });
      this.plotList = this.plotList.map(item => {
        item.hidden = 0;
        return item;
      });
    },
    revealPlot(word) {
      const index = this.plotList.indexOf(word);
      this.plotList[index].hidden = 0;
    },
    getCast() {
      this.castList = this.movie.movie_cast.slice(0, 49);
    },
    // methods used by getmovies, getspecificmovies
    getList(movie) {
      let cnt = 0;
      this.keywordsList = movie.movie_keywords.map(item => {
        cnt++;
        const keywordinfo = {
          id: item.id,
          content: item.content,
          hiddencontent: "-".repeat(item.content.length), // �
          hidden: parseInt(cnt % 6) // 1
        };
        return keywordinfo;
      });
      cnt = 0;
      this.plotList = movie.plot.split(" ").map(item => {
        cnt++;
        const plotinfo = {
          id: item.index,
          content: item,
          hiddencontent: "█".repeat(item.length),
          hidden: parseInt(cnt % 6) // 1
        };
        return plotinfo;
      });
      this.genreList = movie.movie_genres.map(item => {
        const genreinfo = {
          id: item.id,
          content: item.content,
          hidden: 1
        };
        return genreinfo;
      });
    },
    makeHiddenItems(movie) {
      const titleArr = movie.title.split(" ");
      const title = titleArr
        .map(word => {
          return "�".repeat(word.length);
        })
        .join(" ");
      this.hiddenItems = {
        hidden: 1,
        title
      };
    },
    getUserInfo() {
      const token = this.$session.get("jwt");
      this.userinfo = jwtDecode(token);
      console.log(this.userinfo);
    },
    revealifSeenmovie() {
      console.log(this.userinfo.user_id);
      console.log(
        "seen?",
        this.movie.movie_seen_users.some(item => {
          return item.id === this.userinfo.user_id;
        })
      );
      if (
        this.movie.movie_seen_users.some(item => {
          return item.id === this.userinfo.user_id;
        })
      ) {
        this.revealAll();
      }
    },
    seenMovies() {
      console.log("seen Movies");
      const token = this.$session.get("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      const data = {};
      axios
        .post(
          `https://final-be.herokuapp.com/api/v1/movies/${this.movie.id}/seen/`,
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
  beforeMount() {
    this.getUserInfo();
    if (!this.$route.query.movie_pk) {
      console.log("general");
      this.getMovies();
    } else {
      console.log("specific", this.$route.query);
      const q = this.$route.query.movie_pk;
      this.getSpecificMovie(q);
    }
  }
  // mounted() {

  // }
};
</script>

<style scoped>
.quizitem {
  animation: fadein 1s;
  -moz-animation: fadein 1s; /* Firefox */
  -webkit-animation: fadein 1s; /* Safari and Chrome */
  -o-animation: fadein 1s; /* Opera */
}
@keyframes fadein {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-moz-keyframes fadein {
  /* Firefox */
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadein {
  /* Safari and Chrome */
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-o-keyframes fadein {
  /* Opera */
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>