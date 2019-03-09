<template>
  <div>
    <h2 class="title">Login</h2>
    <p>{{ status }}</p>
    <div class="field is-grouped">
      <div class="control is-expanded">
        <input class="input is-primary" @keyup.enter="send" v-model="login" />
      </div>
      <div class="control">
        <button class="button is-primary" @click="send">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
import ChannelService from '@/services/ChannelService.js'
export default {
  data() {
    return {
      login: null,
      status: ''
    }
  },
  methods: {
    send() {
      if (this.login !== null) {
        ChannelService.postUsername(this.login).then(response => {
          if (response.data.status !== 'ok') {
            this.status = response.data.status
          } else {
            localStorage.username = response.data.username
            this.$emit('successfulLogin')
          }
        })
        this.login = null
      }
    }
  }
}
</script>

<style></style>
