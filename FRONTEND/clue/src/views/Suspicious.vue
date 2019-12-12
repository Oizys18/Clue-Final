<template>
  <div>
    <h1>Suspicious</h1>
    <SuspiciousItem />
  </div>
</template>

<script>
import axios from "axios";
import SuspiciousItem from "@/components/SuspiciousItem.vue"
export default {
  name:"Suspicious",
  components:{
    SuspiciousItem
  },
  data() {
    return {
      username: "",
      movies: {},
      BASE_URL: "https://final-be.herokuapp.com",
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
        .get(`${this.BASE_URL}/api/v1/movies/`, options)
        .then(res => {
          this.movies = res.data;
        });
    },
  },
  mounted() {
    this.getMovies();
  },
}
</script>

<style>

</style>