<script setup lang="ts">
defineProps({
    title: String,
})
</script>

<template>
      <button
        class="action__btn"
      >
        {{ title }}
      </button>
</template>

<style scoped>
.action__btn {
  color: rgb(255, 255, 255);
  border-radius: 15px;
  background: linear-gradient(
    45deg,
    rgb(236, 48, 180) 0%,
    rgb(0, 255, 221) 100%
  );
  padding: 15px 20px;
  font-size: 18px;
  transition: all 0.3s ease-in;

  &:hover {
    background: linear-gradient(
      45deg,
      rgb(162, 54, 187) 0%,
      rgb(221, 255, 2) 100%
    );
  }
}



.action__btn_active {
  background: linear-gradient(
    45deg,
    rgb(162, 54, 187) 0%,
    rgb(221, 255, 2) 100%
  );
}
</style>