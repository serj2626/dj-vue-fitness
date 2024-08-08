<script setup lang="ts">
import Posts from "@/components/Posts.vue";
</script>

<template>
  <div class="header__block">
      <h3 class="header__title text-3xl text-center text-white font-extrabold">
        Начни сейчас <br />и никогда не останавливайся.
      </h3>
      <Posts />
    </div>
</template>


<style scoped>
.header {
  position: absolute;
  top: 0;
  background: linear-gradient(45deg, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
    url(../assets/img/home-bg.jpg);

  background-size: cover;
  background-position: center;

  background-repeat: no-repeat;
  width: 100%;
  min-height: 120vh;
}

.header__block {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>