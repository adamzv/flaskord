<template>
  <div>
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
      channel: 'default',
      messages: [],
      msg: null,
      test: {}
    }
  },
  created() {
    ChannelService.getMessages(this.channel).then(response => {
      this.messages = response.data.messages
    })
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
        channel: 'default',
        message: this.msg,
        author: 'admin'
      })
      console.log(this.msg)
    }
  }
}
</script>

<style></style>
