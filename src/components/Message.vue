<template>
  <div>
    <div class="box padding">
      <article class="media">
        <div class="media-content">
          <div class="content">
            <p>
              <strong>{{ message.author }}:</strong>
              {{ message.message }}
            </p>
            <div class="level-right">
              <p>{{ fixedTime }}</p>
            </div>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      fixedTime: null
    }
  },
  props: {
    message: Object
  },
  created() {
    // I could not convert message.time into local time with moment vue filter
    this.fixedTime = this.$moment
      .utc(this.message.time)
      .local()
      .format('MMM Do [|] HH:mm')
  }
}
</script>

<style>
.padding {
  padding: 1rem;
}
</style>
