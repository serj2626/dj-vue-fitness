<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";
import type { IAbonement } from "@/types/orders";


const toast = useToast();
const abonements = ref<IAbonement[]>([]);

const getAbonements = async (): Promise<void> => {
  try {
    const { data } = await axios.get("/api/orders/abonements/");
    abonements.value = data;
  } catch (err) {
    toast.error("Произошла ошибка");
  }
};
onMounted(() => getAbonements());
</script>

<template>
  <h1 class="text-3xl text-center text-uppercase text-yellow-300">
    Абонементы
  </h1>

  <div class="flex justify-center items-center gap-10 mt-10 mb-20 text-yellow-400">
    <div v-for="abonement in abonements" :key="abonement.id"
      class="box flex flex-col gap-2 items-center justify-around">
      <div class="box__title">
        <h3 class="title text-xl uppercase font-bold">{{ abonement.title }}</h3>
      </div>
      <div class="box__body text-center">
        <p class="text-white mb-4">{{ abonement.description }}</p>
        <span class="text-gray-400">{{ abonement.price }} рублей</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.box {
  width: 300px;
  height: 300px;

  /* transition: all 0.3s ease-in; */
  border-radius: 10px;
  font-size: 18px;
  box-shadow: 0 0 15px rgba(255, 255, 255, 0.918);
  padding: 15px;

  /* &:hover {
    transform: scale(1.1);
  } */
}

.box:nth-child(1) {
  background: linear-gradient(45deg,
      rgb(0, 0, 0) 0%,
      rgba(188, 11, 94, 0.917) 50%);
  animation: show-one linear both;
  animation-timeline: view();
}

.box:nth-child(2) {
  background: linear-gradient(45deg,
      rgb(4, 4, 4) 5%,
      rgba(255, 177, 31, 0.917) 100%);
  animation: show-two linear both;
  animation-timeline: view();
}

.box:nth-child(3) {
  background: linear-gradient(45deg,
      rgb(32, 41, 49) 0%,
      rgba(251, 39, 255, 0.917) 100%);
  animation: show-three linear both;
  animation-timeline: view();
}

.box:nth-child(4) {
  background: linear-gradient(45deg,
      rgb(0, 0, 0) 0%,
      rgba(26, 224, 197, 0.917) 100%);

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
