<template>
  <div>
    <h2 class="title">Channels</h2>
    <div class="height-container">
      <nav class="panel">
        <a
          class="panel-block is-active"
          v-for="channel in channels"
          :key="channel"
          @click="selectChannel(channel)"
          >{{ channel }}</a
        >
      </nav>
    </div>

    <input v-model="enterChannel" />
    <button @click="createChannel">Create channel</button>
  </div>
</template>

<script>
import ChannelService from '@/services/ChannelService.js'

export default {
  data() {
    return {
      enterChannel: null,
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
  },
  methods: {
    createChannel() {
      this.$socket.emit('create channel', { channel: this.enterChannel })
      this.enterChannel = null
    },
    selectChannel(channel) {
      console.log(channel)
      this.lastChannel = channel
      this.$root.$emit('change_selected_channel', channel)
    }
  },
  sockets: {
    newChannel(data) {
      this.lastChannel = data.channel
      this.channels.push(data.channel)
    }
  }
}
</script>

<style></style>
