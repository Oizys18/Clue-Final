<template>
  <div style="margin-left:10px">
    <div>
      <vs-tabs alignment="center">
        <vs-tab label="Seen">
          <div class="row mx-5">
            <div
              class="Mcolumn"
              v-for="movie in seen_movies"
              :key="movie.title"
            >
              <span class="m-title font-noto ">
                {{ movie.title }}
              </span>
              <img :src="movie.poster_url" alt="movie.poster_url" />
            </div>
          </div>
        </vs-tab>
        <vs-tab label="Liked">
          <div class="row mx-5">
            <div
              class="Mcolumn"
              v-for="movie in like_movies"
              :key="movie.title"
            >
              <span class="m-title font-noto ">
                {{ movie.title }}
              </span>
              <img :src="movie.poster_url" alt="movie.poster_url" />
            </div>
          </div>
        </vs-tab>
      </vs-tabs>
    </div>
  </div>
</template>
<script>
import jwtDecode from "jwt-decode";
import router from "@/router";
import axios from "axios";

export default {
  name: "UserDetail",

  data() {
    return {
      like_movies: {},
      seen_movies: {},
      userinfo: "",
      movies: {},
      BASE_URL: "https://final-be.herokuapp.com",
      colorLoading: "#7d0c3f"
    };
  },
  methods: {
    solve(movieKey) {
      router.push(`/quiz?movie_pk=${movieKey}`);
    },
    get_like_movies() {
      this.$vs.loading({ color: this.colorLoading });
      const token = this.$session.get("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      const user_id = jwtDecode(token).user_id;
      axios
        .get(
          `${this.BASE_URL}/api/v1/accounts/${user_id}/like_movies/`,
          options
        )
        .then(res => {
          this.like_movies = res.data.sort(function(a, b) {
            var sortingField = "id";
            return a[sortingField] - b[sortingField];
          });

          this.$vs.loading.close();
        });
    },
    get_seen_movies() {
      this.$vs.loading();
      const token = this.$session.get("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      const user_id = jwtDecode(token).user_id;
      axios
        .get(
          `${this.BASE_URL}/api/v1/accounts/${user_id}/seen_movies/`,
          options
        )
        .then(res => {
          this.seen_movies = res.data.sort(function(a, b) {
            var sortingField = "id";
            return a[sortingField] - b[sortingField];
          });
          this.$vs.loading.close();
        });
    },
    getUserInfo() {
      const token = this.$session.get("jwt");
      this.userinfo = jwtDecode(token).user_id;
    },
    getMovies() {
      const token = this.$session.get("jwt");
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios.get(`${this.BASE_URL}/api/v1/movies/`, options).then(res => {
        this.movies = res.data.sort(function(a, b) {
          var sortingField = "id";
          return a[sortingField] - b[sortingField];
        });
      });
    }
  },
  mounted() {
    this.get_like_movies();
    this.get_seen_movies();
    this.getMovies();
    this.getUserInfo();
  }
};
</script>

<style scoped>
.Mcolumn {
  position: relative;
  overflow: hidden;
  flex: 11%;
  max-width: 11%;
  height: auto;
  padding: 0 4px;
}
.row {
  display: flex;
  flex-wrap: wrap;
  padding: 0 4px;
}
.m-title {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
  height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.4);

  color: rgb(255, 255, 255);
  font-size: 1rem;
  font-weight: bold;
  /* text-decoration: none; */

  display: flex;
  align-items: center;
  justify-content: center;

  opacity: 0;
  transition: opacity 0.5s;
}
.m-title2 {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1;
  height: 100%;
  width: 100%;
  background: rgba(24, 66, 24, 0.4);
  color: rgb(0, 0, 0);
  font-size: 3rem;
  font-weight: bold;
  /* text-decoration: none; */
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 1;
  transition: opacity 0.5s;
}
.Mcolumn:hover .m-title2 {
  opacity: 0;
}
.Mcolumn:hover .m-title {
  opacity: 1;
}
.Mcolumn {
  position: relative;
  overflow: hidden;
  flex: 11%;
  max-width: 11%;
  height: auto;
  padding: 0 4px;
}

.Mcolumn img {
  margin-top: 8px;
  vertical-align: middle;
  width: 100%;
  line-height: 0;
  filter: blur(0px);
  transition: filter 0.3s ease-in;
  transform: scale(1.1);
}

.Mcolumn:hover .Mcolumn img {
  filter: blur(2px);
}

/* Responsive layout - makes a two column-layout instead of four columns */
@media screen and (max-width: 1500px) {
  .Mcolumn {
    flex: 20%;
    max-width: 20%;
  }
  .m-title {
    font-size: 1.3rem;
  }
}

/* Responsive layout - makes a two column-layout instead of four columns */
@media screen and (max-width: 1200px) {
  .Mcolumn {
    flex: 30%;
    max-width: 30%;
  }
  .m-title {
    font-size: 1.5rem;
  }
}

/* Responsive layout - makes a two column-layout instead of four columns */
@media screen and (max-width: 800px) {
  .Mcolumn {
    flex: 50%;
    max-width: 50%;
  }
  .m-title {
    font-size: 1.7rem;
  }
}

/* Responsive layout - makes the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 600px) {
  .Mcolumn {
    flex: 100%;
    max-width: 100%;
  }
  .m-title {
    font-size: 2rem;
  }
}

/* for touch screen devices */
@media (hover: none) {
  .Mcolumn-title {
    opacity: 90%;
  }
  .Mcolumn img {
    filter: blur(2px);
  }
  .m-title {
    font-size: 2rem;
  }
}
</style>
