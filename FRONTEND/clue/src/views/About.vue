<template>
  <div class="about-body">
    <div>
      <vs-row>
        <vs-col vs-type="flex" vs-justify="center" vs-align="center">
          <div class="m-2 p-2">
            <h1 class="gate" style="font-size:120px; color:white">About us</h1>
          </div>
        </vs-col>
      </vs-row>
    </div>
    <div>
      <vs-row>
        <vs-col vs-type="flex" vs-justify="center" vs-align="center">
          <vs-chip class="m-3" color="primary">
            <span>Nov22.2019 10:01am ~ Nov29.2019 06:24am</span>
          </vs-chip>
        </vs-col>
      </vs-row>
    </div>
    <vs-row>
      <vs-col vs-type="flex" vs-justify="center" vs-align="center">
        <div class="about-card   p-2">
          <iframe
            width="560"
            height="315"
            src="https://www.youtube.com/embed/0n2ItsCmLtw?rel=0;&autoplay=1&loop=1"
            frameborder="0"
            allowfullscreen
            include
          ></iframe>
          <vs-row>
          <vs-chip size=large class="tag" color="dark">
            <span>🔺영혼을 떠나보내는 육신</span>
          </vs-chip>
          </vs-row>
        </div>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
export default {
  name: "About",
  methods: {}
};
</script>

<style scoped>
.about-body {
  color: black;
  width: 100%;
  height: 100vh;
  background: linear-gradient(180deg, #3a1c71, #d76d77, #ffaf7b);
  background-size: 100% 200%;
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
.tag{
    position: relative;
}
</style>
