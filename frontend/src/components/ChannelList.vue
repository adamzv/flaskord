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
      channels: []
    }
  },
  created() {
    ChannelService.getChannels()
      .then(response => {
        this.channels = response.data.channels
        console.log(response)
      })
      .catch(error => {
        console.log(error.response)
      })
  }
}
</script>

<style></style>
