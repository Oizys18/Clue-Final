<template>
  <div class="Login">
    <LoginForm />
  </div>
</template>

<script>
import LoginForm from "@/components/LoginForm.vue";

export default {
  name: "Login",
  components: {
    LoginForm
  }
};
</script>

<style scoped>
.Login {
  margin: 0;
  padding-top: 10%;
  width: 100%;
  height: 100vh;
  color: black;
  background: linear-gradient(-45deg, #3e5151, #decba4);
  background-size: 600% 500%;
  animation: gradientBG 5s ease infinite;
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
