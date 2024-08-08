<script setup lang="ts">
import Posts from "@/components/Posts.vue";
</script>

<template>
  <div class="header__block">
      <h3 class="header__title text-3xl mb-16 text-center text-white font-extrabold">
        Начни сейчас <br />и никогда не останавливайся.
      </h3>
      <Posts />
    </div>
</template>


<style scoped>
.header__block {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>