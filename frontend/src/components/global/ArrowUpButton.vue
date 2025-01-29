<script setup lang="ts">
function backToTop() {
  window.scrollTo({ top: 0, behavior: "smooth" });
}
</script>

<template>
  <!-- <a @click="backToTop"
    ><i class="fa-solid fa-arrow-up fa-beat fa-2xl" style="color: #ffd43b"></i>
  </a> -->


  <button @click="backToTop" class="back-to-top" title="Наверх">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
      <path d="M0 0h24v24H0V0z" fill="none"/>
      <path d="M4 12l1.41 1.41L11 7.83V20h2V7.83l5.59 5.59L20 12l-8-8-8 8z"/>
    </svg>
  </button>
</template>

<style scoped lang="scss">
i {
  cursor: pointer;
  position: fixed;
  bottom: 50px;
  right: 50px;
  color: #ffd43b;
}

.back-to-top {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background-color: #f2f205;
  border: none;
  padding: 10px;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.back-to-top svg {
  fill: #333;
}
</style>
