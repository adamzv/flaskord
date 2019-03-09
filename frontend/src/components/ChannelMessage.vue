<template>
  <div>
    <h1>#{{ last_channel }}</h1>
    <Message v-for="message in messages" :key="message.id" :message="message" />
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
      msg: null,
      test: {}
    }
  },
  created() {
    ChannelService.getMessages(this.lastChannel).then(response => {
      this.messages = response.data.messages
    })
  },
  mounted() {
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
      console.log(data)
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
    }
  }
}
</script>

<style></style>
