<template>
  <div class="home">
    <LoginForm greeting="Greeting"/>
  </div>
</template>

<script>
// @ is an alias to /src
import LoginForm from "@/components/LoginForm.vue"

import BASEURL from "../Const"

import axios from "axios"

export default {
  name: 'home',
  components: {
    LoginForm
  },
  data () {
    return {
      logged: false
    }
  },
  mounted () {
    console.log(BASEURL)
    axios.get(
      BASEURL
    ).then(response => {
      // console.log(response.data)
      self.logged = response.data
    }).catch(error => {
      console.log(error)
    })
  }
}

</script>
