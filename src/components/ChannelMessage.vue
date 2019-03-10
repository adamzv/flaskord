<template>
  <div>
    <h2 class="title">
      <span class="has-text-grey-light">#</span>
      {{ lastChannel }}
    </h2>
    <div id="chat" class="card height-container">
      <Message
        v-for="message in messages"
        :key="message.id"
        :message="message"
      />
    </div>
    <br />
    <div class="field is-grouped">
      <div class="control is-expanded">
        <input class="input is-primary" v-model="msg" @keyup.enter="send" />
      </div>
      <div class="control">
        <button class="button is-primary" @click="send">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
import Message from '@/components/Message.vue'
import ChannelService from '@/services/ChannelService.js'
export default {
  data() {
    return {
      author: null,
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
    this.author = localStorage.username
  },
  components: {
    Message
  },
  sockets: {
    disconnect() {
      this.message = []
    },
    newMessage(data) {
      this.messages.push(data)
      // store only 100 messages per channel
      if (this.messages.length > 100) {
        this.messages.shift()
      }
    }
  },
  methods: {
    send() {
      if (this.msg !== null) {
        this.$socket.emit('send msg', {
          channel: this.lastChannel,
          message: this.msg,
          author: this.author
        })
        this.msg = null
      }
    }
  },
  watch: {
    lastChannel(newChannel) {
      localStorage.lastChannel = newChannel
    },
    messages() {
      this.$nextTick(() => {
        var container = this.$el.querySelector('#chat')
        container.scrollTop = container.scrollHeight + 500
      })
    }
  }
}
</script>

<style></style>
