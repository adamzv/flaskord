<template>
  <div>
    <h2 class="title">#{{ lastChannel }}</h2>
    <div class="height-container">
      <Message
        v-for="message in messages"
        :key="message.id"
        :message="message"
      />
    </div>

    <input v-model="msg" />
    <button @click="send">Send</button>
  </div>
</template>

<script>
import Message from '@/components/Message.vue'
import ChannelService from '@/services/ChannelService.js'
// vue-cookie? vue-session? ziska author a channel
export default {
  data() {
    return {
      lastChannel: 'default',
      messages: [],
      msg: null
    }
  },
  created() {
    ChannelService.getMessages(this.lastChannel).then(response => {
      this.messages = response.data.messages
    })
  },
  mounted() {
    // using root Vue instance as global Event Hub to pass selected channel from ChannelList.vue component
    this.$root.$on('change_selected_channel', channel => {
      this.lastChannel = channel
      ChannelService.getMessages(channel).then(response => {
        this.messages = response.data.messages
      })
    })
    if (localStorage.lastChannel) {
      this.lastChannel = localStorage.lastChannel
    }
  },
  components: {
    Message
  },
  sockets: {
    connect() {
      console.log('connected')
    },
    disconnect() {
      this.message = []
    },
    newMessage(data) {
      this.messages.push(data)
    }
  },
  methods: {
    send() {
      this.$socket.emit('send msg', {
        channel: this.lastChannel,
        message: this.msg,
        author: 'admin'
      })
      this.msg = null
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
