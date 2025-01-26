<script lang="ts" setup></script>

<template>
  <section id="women" class="women"></section>
</template>

<style lang="scss" scoped>
.women {
  background-image: url(../../assets/img/fitness1.png);
  background-attachment: local;
  background-size: cover;
  height: 700px;

  background-repeat: no-repeat;

  animation: women-opacity linear both;
  animation-timeline: view();
}

@keyframes women-opacity {
  0% {
    opacity: 0;
  }

  70% {
    opacity: 1;
  }
}
</style>
