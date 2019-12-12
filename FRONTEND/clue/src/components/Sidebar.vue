<template>
  <vs-sidebar
    @mouseleave="active = false"
    parent="body"
    default-index="1"
    color="warning"
    class="sidebarx"
    spacer
    v-model="sbactive"
  >
    <div class="header-sidebar" slot="header">
      <h3 class="font-bungee">CLUE</h3>
    </div>
    <div v-if="userisActive">
      <vs-sidebar-item index="1" to="/quiz">Quiz</vs-sidebar-item>
      <vs-sidebar-item index="2" to="/quizlist">Quizlist</vs-sidebar-item>
      <vs-sidebar-item index="3" to="/userdetail">myInfo</vs-sidebar-item>
      <vs-sidebar-item index="4" @click="clickLogout()">logout</vs-sidebar-item>
    </div>
    <div v-else>
      <vs-sidebar-item index="1" to="/login">Login</vs-sidebar-item>
    </div>
    <vs-sidebar-item index="5" to="/about">About</vs-sidebar-item>
  </vs-sidebar>
</template>

<script>
export default {
  name: "Sidebar",
  props: {
    sbactive: {
      type: Boolean,
      required: true,
    },
    userisActive: {
      type: Boolean,
      required: true,
    }
  },
  methods: {
    clickLogout() {
      this.$emit("onlogout")
    },
    sbActiveChange() {
      this.$emit("onSbChange")
    },
    sidebarEvent() {
      const sb = document.querySelector(".vs-sidebar");
      sb.addEventListener("mouseleave", () => {
        if (screen.width > 576) {
          this.sbActiveChange()
        } else if (screen.height < 576 && screen.width < 800) {
          this.sbActiveChange()
        }
      });
    }
  },
  mounted() {
    this.sidebarEvent();
  },
  updated() {
    console.log('is user active?',this.userisActive)
  }
};
</script>

<style scoped>
.header-sidebar {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  width: 100%;
}
h4 {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}
h4 > button {
  margin-left: 10px;
}

.footer-sidebar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}
.footer-sidebar > button {
  border: 0px solid rgba(0, 0, 0, 0) !important;
  border-left: 1px solid rgba(0, 0, 0, 0.07) !important;
  border-radius: 0px !important;
}
</style>