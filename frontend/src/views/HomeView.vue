<script setup lang="ts">
import Subscribe from "../components/Subscribe.vue";
import Coach from "../components/Coach.vue";
import Abonements from "@/components/Abonements.vue";
import About from "@/components/About.vue";
</script>

<template>
  <ArrowUpButton />
  <section id="header" class="header relative">
    <div class="header__block">
      <h3 class="header__title text-3xl text-center text-white font-extrabold">
        Начни сейчас <br />и никогда не останавливайся.
      </h3>
      <div class="grid grid-cols-5 gap-5 mt-16">
        <div class="grid__box">Спина</div>
        <div class="grid__box">Грудь</div>
        <div class="grid__box">Руки</div>
        <div class="grid__box">Ноги</div>
        <div class="grid__box">Плечи</div>
      </div>
    </div>
  </section>
  <section id="about" class="about container text-purple-500">
    <About />
  </section>
  <section id="abonements" class="container abonements  mt-16">
    <Abonements />
  </section>
  <div class="women">

  </div>
  <section id="training" class="training container">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quisquam
    reprehenderit qui tenetur non aliquam ullam totam? Doloremque assumenda impedit modi dolorem porro natus sunt vitae,
    soluta ab maiores aliquam officia, doloribus aspernatur accusamus ducimus? laudantium dignissimos repellendus amet
    aliquid! Veritatis asperiores iste Excepturi obcaecati molestias quibusdam modi dolores adipisci pariatur animi
    quae. Eligendi velit eveniet reiciendis beatae corrupti, voluptas ut aliquid fugit assumenda repellendus, non
    tempora deserunt.</section>

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
  background: linear-gradient(45deg, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
    url(../assets/img/home-bg.jpg);

  background-size: cover;
  /* background-position: center; */

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

.pool {
  background-image: url(../assets/img/fitness-pool.jpg);
  background-attachment: fixed;
  background-size: cover;
  height: 500px;
}

.women {
  background-image: url(../assets/img/fitness1.png);
  background-attachment: local;
  height: 700px;

  background-repeat: no-repeat;
}
</style>
