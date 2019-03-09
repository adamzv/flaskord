<template>
  <div>
    <nav class="panel">
      <a
        class="panel-block is-active"
        v-for="channel in channels"
        :key="channel"
        >{{ channel }}</a
      >
    </nav>
  </div>
</template>

<script>
import ChannelService from '@/services/ChannelService.js'

export default {
  data() {
    return {
      lastChannel: 'default',
      channels: []
    }
  },
  created() {
    ChannelService.getChannels()
      .then(response => {
        this.channels = response.data.channels
      })
      .catch(error => {
        console.log(error.response)
      })
  },
  mounted() {
    if (localStorage.lastChannel) {
      if (this.lastChannel in this.channels === true) {
        this.lastChannel = localStorage.lastChannel
      }
    }
  },
  watch: {
    lastChannel(newChannel) {
      localStorage.lastChannel = newChannel
    }
  }
}
</script>

<style></style>
