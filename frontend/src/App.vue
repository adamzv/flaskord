<template>
  <div id="app">
    <div class="columns">
      <div class="column is-one-third">
        <ChannelList />
      </div>
      <div class="column">
        <ChannelMessage />
      </div>
    </div>
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

<style lang="css">
@import './assets/styles/styles.css';
@import '~bulma/css/bulma.css';
</style>
