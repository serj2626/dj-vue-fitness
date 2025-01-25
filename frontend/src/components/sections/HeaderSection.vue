<script lang="ts" setup></script>

<template>
  <section id="header" class="header-section">
    <div class="header-section__body">
      <h3
        class="header-section__title text-3xl mb-16 text-center text-white font-extrabold"
      >
        Начни сейчас <br />и никогда не останавливайся.
      </h3>
      <!-- <Posts /> -->
    </div>
  </section>
</template>

<style lang="scss" scoped>
.header-section {
  position: relative;
  top: 0;
  background: linear-gradient(45deg, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
    url(../../assets/img/home-bg.jpg);

  background-size: cover;
  background-position: center;

  background-repeat: no-repeat;
  width: 100%;
  min-height: 120vh;
}


.header-section__body {
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
