<template>
  <div>
    <div>
      <p>{{ message.author }}</p>
      <p>{{ message.message }}</p>
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
