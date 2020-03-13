<template>
  <div>
    <div class="sidebar" @mouseenter="sbactive = true"></div>
    <div class="mainapp">
      <Sidebar
        :sbactive="sbactive"
        :userisActive="userisActive"
        @onlogout="logout"
        @onSbChange="sbactive = !sbactive"
      />
      <router-view />
    </div>
    <!-- <vs-row class="m-2">
      <vs-col vs-w="0" vs-xs="12"></vs-col>
    </vs-row> -->
    <div class="extra">
      <vs-button size="small" color="primary" @click="sbactive = !sbactive"
        >sidebar ></vs-button
      >
    </div>
    <!-- vs-avatar
      <div class="footer">
      <vs-chip class="badge-color0">
        <vs-avatar text="🐧" class="badge-avatar-color3" />
        LEO
      </vs-chip>
    </div> -->
  </div>
</template>

<script>
import axios from "axios";
import router from "@/router";
import Sidebar from "@/components/Sidebar";
import "material-icons/iconfont/material-icons.css";

export default {
  name: "app",
  data() {
    return {
      sbactive: false,
      userisActive: false,
      BASE_URL: "http://127.0.0.1:8000"
    };
  },
  components: {
    Sidebar
  },
  methods: {
    loggedIn() {
      this.$session.start();
      if (!this.$session.has("jwt")) {
        router.push("/login").catch(err => {
          err;
        });
      } else {
        this.userisActive = true;
      }
    },
    userCheck() {
      this.userisActive = this.$session.has("jwt");
    },
    logout() {
      if (this.$session.has("jwt")) {
        const token = this.$session.get("jwt");
        const options = {
          headers: {
            Authorization: "JWT " + token
          }
        };
        axios.post(`${this.BASE_URL}/rest-auth/logout/`, options).then(res => {
          this.$session.remove("jwt");
          router.push("/login");
          this.$vs.notify({
            title: "Logged out",
            text: res.data.detail,
            color: "dark",
            fixed: true,
            click: () => {
              // Secondary function
              this.$vs.notify({
                title: "Good bye!",
                text: "Login again",
                color: "warning"
              });
            }
          });
        });
      }
    }
  },
  mounted() {
    this.loggedIn();
  },
  updated() {
    this.userCheck();
  }
};
</script>
<style>
.font-noto {
  font-family: "Noto Sans", sans-serif;
}
.font-source {
  font-family: "Source Sans Pro", sans-serif;
}
.font-bungee {
  font-family: "Bungee Shade", cursive;
}
.mainapp {
  margin-left: 7px;
}
@media (max-width: 576px) {
  .extra {
    position: fixed;
    bottom: 5px;
    right: 5px;
    display: unset !important;
  }
}
@media (max-height: 576px) {
  .extra {
    position: fixed;
    bottom: 5px;
    right: 5px;
    display: unset !important;
  }
}
.extra {
  display: none;
}
body {
  background-color: #e3e3cf;
}
.sidebar {
  background-color: rgba(255, 186, 0, 0.5);
  width: 7px;
  height: 100%;
  position: fixed;
}
</style>
