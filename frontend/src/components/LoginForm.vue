<template>
  <div class="form-group">
    <form @submit.prevent="login">
      <label for="username">Username</label>
      <input
        type="text"
        name="username"
        id="username"
        class="form-control"
        v-model="form.username"
        required
      />
      <br />
      <label for="password">Password</label>
      <input
        type="password"
        name="password"
        id="password"
        class="form-control"
        v-model="form.password"
        required
      />
      <br />
      <div class="text-center">
        <div class="btn-group mr-2">
          <button type="submit" class="btn btn-primary">Login</button>
        </div>
        <div class="btn-group mr-2">
          <button type="button" class="btn btn-danger">Register</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios"

import BASEURL from "../Const"

export default {
  name: "LoginForm",
  data () {
    return {
      form: {
        username: '',
        password: '',
      }
    }
  },
  methods: {
    login () {
      var name = this.form.username
      var pass = this.form.password
      //   alert(name)
      //   alert(pass)

      var url = BASEURL + "login"
      axios.post(url, {
        name: name,
        pass: pass
      }).then(response => {
        console.log(response.data)
      }).catch(error => {
        console.log(error.toJSON())
      })
    }
  },
  props: {
    username: String,
    password: String
  }
}
</script>

<style scoped>
input {
  width: 30%;
  margin: 0 auto;
}
</style>