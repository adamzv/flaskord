<template>
  <div id="app">
    <button class="button is-primary">This is a button</button>
    <ChannelList />
    <ChannelMessage />
  </div>
</template>

<script>
import ChannelList from '@/components/ChannelList.vue'
import ChannelMessage from '@/components/ChannelMessage.vue'

export default {
  components: {
    ChannelList,
    ChannelMessage
  }
}
</script>

<style>
@import '~bulma/css/bulma.css';
</style>
