<template>
  <div>
    <div>
      <p>{{ message.author }}</p>
      <p>{{ message.message }} | {{ message.time }}</p>
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

<style></style>
