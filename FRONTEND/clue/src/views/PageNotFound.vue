<template>
  <div class="zoobody">
    <div>
      <vs-row>
        <vs-col vs-type="flex" vs-justify="center" vs-align="center">
        <div class="shadow rounded bg-white m-2 p-4">
          <h1>Page Not Found!! GO BACK!</h1>
          <small>...But before that, check out these cuties.</small>
        </div>
        </vs-col>
        <vs-col vs-type="flex" vs-justify="center" vs-align="center" class="pb-3">
          <vs-button class="m-1" color="dark" type="relief" @click="catdog()" 
            >I Like it! Another!</vs-button
          >
        </vs-col>
      </vs-row>
    </div>

    <vs-row>
      <vs-col vs-type="flex" vs-justify="center" vs-align="center">
        <div class="zoo shadow rounded bg-white p-5">
          <img
            class="cat rounded flex img-thumbnail"
            :src="catIMG"
            alt="catIMG"
          />
          <img
            class="dog rounded flex img-thumbnail"
            :src="dogIMG"
            alt="dogIMG"
          />
        </div>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "PageNotFound",
  data() {
    return {
      dogIMG: "",
      catIMG: "",
      catURL: "https://api.thecatapi.com/v1/images/search",
      dogURL: "https://dog.ceo/api/breeds/image/random"
    };
  },
  methods: {
    catdog() {
      axios.get(this.dogURL).then(res => {
        this.dogIMG = res.data.message;
      })
      axios.get(this.catURL).then(res => {
        this.catIMG = res.data[0].url;
      });
    }
  },
  beforeMount() {
    this.catdog();
  }
};
</script>

<style scoped>
.cat {
  margin:5px;
  width: 300px;
  height: 300px;
}
.dog {
  margin:5px;
  width: 300px;
  height: 300px;
}
.zoo {
  color: black;
  background: linear-gradient(-45deg,#0221cf, #ff0000,#ff8800,#00ff40,#002fff, #f700ff);
  background-size: 300% 600%;
  animation: gradientBG 0.4s ease infinite;
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
.zoobody{
  color: black;
  width:100%;
  height:100vh;
  background: linear-gradient(45deg,#0221cf, #ff0000,#ff8800,#00ff40,#002fff, #f700ff);
  background-size: 300% 600%;
  animation: gradientBG 1s ease infinite;
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
