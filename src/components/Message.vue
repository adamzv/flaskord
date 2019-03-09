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
              <p>{{ message.time }}</p>
            </div>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    message: Object
  }
}
</script>

<style>
.padding {
  padding: 1rem;
}
</style>
