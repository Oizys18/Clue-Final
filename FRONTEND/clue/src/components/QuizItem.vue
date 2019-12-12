<template>
  <div>
    <vs-row>
      <vs-col vs-type="flex" vs-justify="center" vs-align="center">
        <div v-if="!hiddenItems.hidden">
          <div>
            <h1 class="d-inline-block">{{ movie.title }}</h1>
            <span>({{ movie.year }})</span>
          </div>
        </div>
        <div v-else>
          <div>
            <h1 class="d-inline-block" @click="revealAll">{{ hiddenItems.title }}</h1>
            <span>(xxxx)</span>
          </div>
        </div>
      </vs-col>
      <vs-col vs-type="flex" vs-justify="center" vs-align="center">
        <div>
          <vs-chip class="badge-color2" v-for="genre in genreList" :key="genre.id">
            <vs-avatar text="G" class="badge-avatar-color2"/>
            {{ genre.content }}
          </vs-chip>
        </div>
      </vs-col>
    </vs-row>
    <vs-row>
      <vs-col vs-type="flex">
        <div>
          <vs-divider color="#9D3D12" position="left-center"><span>keywords</span></vs-divider>
          <span id="keywordItem" v-for="keyword in keywordsList.slice(0,20)" :key="keyword.id">
            <span class="badge" v-if="!keyword.hidden">{{ keyword.content }}</span>
            <span class="badge badge-color1 mr-1" @click="revealKey(keyword)" v-else>{{ keyword.hiddencontent }}</span>
          </span>
        </div>
      </vs-col>
      <vs-col vs-type="flex">
        <div class="my-2">
          <vs-divider color="#ffb61c" position="right-center"><span class="text-weight-bold">plot</span></vs-divider>
          <span v-for="plot_word in plotList" :key="plot_word.id">
            <span v-if="!plot_word.hidden" class="text-color-yellow">{{ plot_word.content }} </span>
            <span class="badge text-color-yellow"  v-else @click="revealPlot(plot_word)">{{ plot_word.hiddencontent }}</span>
          </span>
        </div>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
export default {
  name: "QuizItem",
  data() {
    return {
    };
  },
  props: {
    movie: {
      type: Object,
      required: true
    },
    hiddenItems: {
      type: Object,
      required: true
    },
    keywordsList: {
      type: Array,
      required: true
    },
    plotList: {
      type: Array,
      required: true
    },
    genreList: {
      type: Array,
      required: true
    },
  },
  methods: {
    revealKey(keyword) {
      this.$emit("onRevealKey", keyword)
    },
    revealAll() {
      this.$emit("onRevealAll")
    },
    revealPlot(word) {
      this.$emit("onRevealPlot", word)
    },
  },
};
</script>
<style scoped>
  .badge-color1 {
    background-color: #4C1B02;
    color: white
  }
  .badge-color2 {
    background-color: #D17534!important;
    color: black;
    font-weight: bold;
  }
  .badge-avatar-color2 {
    background-color: #741D06!important;
    color: #CFB06F!important;
    cursor: initial!important;
  }
  .text-color-yellow {
    color: #ffb61c;
  }
  
</style>
