<template>
  <div>
    <vs-row vs-justify="center">
      <vs-col
        vs-justify="center"
        vs-align="center"
        vs-w="4"
        vs-sm="6"
        vs-xs="12"
        class="mx-4"
      >
      <h1 class="mt-0">CLUE</h1>
        <div class="shadow rounded bg-white p-4">
          <!-- Login/Signup tabs -->
          <vs-tabs position="right" alignment="center" :color="'dark'">
            
            <vs-tab label="Login">
              <vs-row>
                <vs-col class="mb-1" vs-type="flex" vs-justify="center">
                  <vs-input

                    label-placeholder="Username"
                    v-model="credentials.username"
                    type="text"
                    id="login_id"
                  />
                </vs-col>
                <vs-col vs-type="flex" vs-justify="center">
                  <vs-input
                    label-placeholder="Password"
                    v-model="credentials.password"
                    type="password"
                    id="password"
                  />
                </vs-col>
                <vs-col vs-type="flex" vs-justify="center" >
                  <vs-button
                    color="dark"
                    type="relief"
                    @click="login()"
                    class="mt-4"
                    style="width:5rem;"
                    >Login</vs-button
                  >
                </vs-col>
              </vs-row>
            </vs-tab>
            <vs-tab label="Signup">
              <vs-row>
                <vs-col class="mb-1" vs-type="flex" vs-justify="center">
                  <vs-input
                    label-placeholder="Username"
                    v-model="credentials.username"
                    type="text"
                    id="login_id"
                  />
                </vs-col>
                <vs-col class="mb-1" vs-type="flex" vs-justify="center">
                  <vs-input
                    label-placeholder="Password1"
                    v-model="credentials.password1"
                    type="password"
                    id="password1"
                  />
                </vs-col>
                <vs-col vs-type="flex" vs-justify="center">
                  <vs-input
                    label-placeholder="Password2"
                    v-model="credentials.password2"
                    type="password"
                    id="password2"
                  />
                </vs-col>
                <vs-col vs-type="flex" vs-justify="center">
                  <vs-button
                    color="dark"
                    type="relief"
                    @click="signup()"
                    class="mt-4"
                    style="width:5rem;"
                    >Sign up</vs-button
                  >
                </vs-col>
              </vs-row>
            </vs-tab>
          </vs-tabs>
        </div>
      </vs-col>
    </vs-row>
  </div>
</template>``

<script>
import axios from "axios";
import router from "@/router";

export default {
  name: "LoginForm",
  data() {
    return {
      credentials: {},
      errorMsg: {},
      BASE_URL: "https://final-be.herokuapp.com"
    };
  },
  methods: {
    login() {
      axios
        .post(`${this.BASE_URL}/rest-auth/login/`, this.credentials)
        .then(res => {
          const token = res.data.token;
          this.$session.start();
          this.$session.set("jwt", token);
          router.push("/quiz");
        })
        .catch(err => {
          for (let error in err.response.data){
            this.$vs.notify({
              title:'Validation Error',
              text: `${error}: ${err.response.data[error]}`,
              color:'dark',
            })
          }
        });
    },
    signup() {
      axios
        .post(`${this.BASE_URL}/rest-auth/registration/`, this.credentials)
        .then(res => {
          console.log(res);
          if ("token" in res.data) {
            const token = res.data.token;
            this.$session.start();
            this.$session.set("jwt", token);
            router.push("/quiz");
          }
        })
        .catch(err => {
          for (let error in err.response.data){
            this.$vs.notify({
              title:'Validation Error',
              text: `${error}: ${err.response.data[error]}`,
              color:'dark',
            })
          }
        });
    }
  }
};
</script>

<style>
</style>
