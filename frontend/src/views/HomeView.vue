<script setup lang="ts">
import Subscribe from "../components/Subscribe.vue";
import Coach from "../components/trainer/Coach.vue";
import Abonements from "@/components/Abonements.vue";
import About from "@/components/About.vue";
import BlockHeader from "@/components/BlockHeader.vue";


</script>

<template>
  <ArrowUpButton />
  <section id="header" class="header relative">
    <BlockHeader />
  </section>
  <section id="about" class="about container text-purple-500">
    <About />
  </section>
  <section id="abonements" class="container abonements mt-16">
    <Abonements />
  </section>
  <div class="women"></div>

  <section id="coach" class="coach container text-orange-300 my-14">
    <Coach />
  </section>
  <section id="pool" class="pool"></section>
  <section id="contacts" class="feedback container text-lime-300">
    <Subscribe />
  </section>
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

#about{
 margin-top: 120vh;
 padding-block: 50px;
}

.pool {
  background-image: url(../assets/img/fitness-pool.jpg);
  background-attachment: fixed;
  background-size: cover;

  height: 500px;
}

.women {
  background-image: url(../assets/img/fitness1.png);
  background-attachment: local;
  background-size: cover;
  height: 700px;

  background-repeat: no-repeat;
}
</style>
