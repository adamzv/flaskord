<template>
  <div id="app">
    <div v-if="active">
      <div class="columns">
        <div class="column is-one-third">
          <ChannelList />
        </div>
        <div class="column">
          <ChannelMessage />
        </div>
      </div>
    </div>
    <div v-else>
      <Login v-on:successfulLogin="handleLogin" />
    </div>
  </div>
</template>

<script>
import ChannelList from '@/components/ChannelList.vue'
import ChannelMessage from '@/components/ChannelMessage.vue'
import Login from '@/components/Login.vue'

export default {
  components: {
    ChannelList,
    ChannelMessage,
    Login
  },
  data() {
    return {
      active: null
    }
  },
  created() {
    if (localStorage.username) {
      this.active = true
    }
  },
  methods: {
    handleLogin() {
      this.active = true
    }
  }
}
</script>

<style lang="css">
@import '~bulma/css/bulma.css';
@import './assets/styles/styles.css';
</style>
