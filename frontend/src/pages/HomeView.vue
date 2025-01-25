<script setup lang="ts">
import AboutSection from "@/components/sections/AboutSection.vue";
import CoachList from "../components/trainer/CoachList.vue";
import Abonements from "@/components/abonements/Abonements.vue";
import HeaderSection from "@/components/sections/HeaderSection.vue";
import SubscribeSection from "@/components/sections/SubscribeSection.vue";
import PoolSection from "@/components/sections/PoolSection.vue";
</script>

<template>
  <ArrowUpButton />
  <HeaderSection />
  <AboutSection />
  <PoolSection />
  <SubscribeSection />
  <!-- <section id="about" class="about container text-white">
    <About />
  </section> -->
  <!-- <section id="abonements" class="container abonements mt-16">
    <Abonements />
  </section> -->
  <!-- <div class="women"></div> -->

  <!-- <section id="coach" class="coach container text-orange-300 my-14">
    <CoachList />
  </section> -->
  <!-- <section id="contacts" class="feedback container text-lime-300">
    <Subscribe />
  </section> -->

</template>
<style scoped lang="scss">


.women {
  background-image: url(../assets/img/fitness1.png);
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
