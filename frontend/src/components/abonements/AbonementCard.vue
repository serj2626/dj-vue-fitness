<script setup lang="ts">
import type { IAbonement } from "./AbonementsList.vue";

defineProps<{
  abonement: IAbonement;
}>();
</script>
<template>
  <div class="abonement abonements__item box flex flex-col gap-2 items-center justify-around">
    <div class="box__title">
      <h3 class="title text-xl uppercase font-bold">{{ abonement.title }}</h3>
    </div>
    <div class="box__body text-center">
      <p class="text-white mb-4">{{ abonement.description }}</p>
      <span class="text-gray-400">{{ abonement.price }} рублей</span>
    </div>
  </div>
</template>
