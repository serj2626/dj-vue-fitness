<script setup lang="ts">
import { onMounted } from "vue";
import AbonementCard from "../abonements/AbonementCard.vue";
import { useAbonementsStore } from "@/stores/abonements";
import { storeToRefs } from "pinia";
import { AppRoutes } from "@/utils/router";
import { useRouter } from "vue-router";


const router = useRouter();
const store = useAbonementsStore();
const { abonements } = storeToRefs(store);
const { getAbonements } = store;
onMounted(getAbonements);
</script>

<template>
  <section id="abonements" class="abonements my-16">
    <div class="container-md abonements__container">
      <h1
        class="abonements__title text-3xl text-center text-uppercase text-yellow-300"
      >
        Абонементы
      </h1>

      <div
        class="abonements__list flex justify-center items-center gap-10 my-20 text-yellow-400"
      >
        <AbonementCard
          v-for="abonement in abonements"
          :key="abonement.id"
          :abonement="abonement"
          @click="router.push(AppRoutes.abonements)"
        />
      </div>
    </div>
  </section>
</template>

<style scoped lang="scss">
.box {
  width: 300px;
  height: 300px;

  border-radius: 10px;
  font-size: 18px;
  box-shadow: 0 0 15px rgba(255, 255, 255, 0.918);
  padding: 15px;
}

.box:nth-child(1) {
  background: linear-gradient(
    45deg,
    rgb(0, 0, 0) 0%,
    rgba(188, 11, 94, 0.917) 50%
  );
  animation: show-one linear both;
  animation-timeline: view();
}

.box:nth-child(2) {
  background: linear-gradient(
    45deg,
    rgb(4, 4, 4) 5%,
    rgba(255, 177, 31, 0.917) 100%
  );
  animation: show-two linear both;
  animation-timeline: view();
}

.box:nth-child(3) {
  background: linear-gradient(
    45deg,
    rgb(32, 41, 49) 0%,
    rgba(251, 39, 255, 0.917) 100%
  );
  animation: show-three linear both;
  animation-timeline: view();
}

.box:nth-child(4) {
  background: linear-gradient(
    45deg,
    rgb(0, 0, 0) 0%,
    rgba(26, 224, 197, 0.917) 100%
  );

  animation: show-four linear both;
  animation-timeline: view();
}

@keyframes show-four {
  0% {
    opacity: 0;
    scale: 0.5;
    transform: translateX(100px);
  }

  40% {
    opacity: 1;
    scale: 1;
    transform: translateX(0);
  }
}

@keyframes show-three {
  0% {
    opacity: 0;
    scale: 0.5;
    transform: translateX(60px);
  }

  60% {
    opacity: 1;
    scale: 1;
    transform: translateX(0);
  }
}

@keyframes show-two {
  0% {
    opacity: 0;
    scale: 0.5;
    transform: translateX(-60px);
  }

  60% {
    opacity: 1;
    scale: 1;
    transform: translateX(0);
  }
}

@keyframes show-one {
  0% {
    opacity: 0;
    scale: 0.5;
    transform: translateX(-100px);
  }

  40% {
    opacity: 1;
    scale: 1;
    transform: translateX(0);
  }
}
</style>
