<script setup lang="ts">
import { onMounted } from "vue";

import CoachCard from "@/components/trainer/CoachCard.vue";
import { FwbInput, FwbSelect } from "flowbite-vue";

import Icon from "@/components/Icon.vue";
import { useCoachesStore } from "@/stores/coaches";
import { storeToRefs } from "pinia";
import { MESSAGES } from "@/types/messages";

const store = useCoachesStore();
const { searchName, selected, categories, allCoaches } = storeToRefs(store);
const { getCoaches } = store;

onMounted(getCoaches);
</script>

<template>
  <div class="container mt-[100px] pt-12 pb-32">
    <div>
      <div class="flex justify-between items-center mb-12">
        <fwb-select
          v-model="selected"
          :options="categories"
          placeholder="Выберите категорию"
          size="sm"
        />
        <h1
          class="text-xl sm:text-2xl md:text-3xl text-center text-uppercase text-yellow-300"
        >
          Тренеры
        </h1>
        <fwb-input v-model="searchName" placeholder="Введите имя тренера">
          <template #prefix>
            <Icon type="search" />
          </template>
        </fwb-input>
      </div>
    </div>
    <div
      v-if="allCoaches.length"
      class="grid max-[450px]:grid-cols-1 grid-cols-2 md:grid-cols-3 gap-10"
    >
      <CoachCard
        v-for="coach in allCoaches"
        :key="coach.id"
        :coach="coach"
      />
    </div>
    <div v-else class="h-[800px] flex justify-center items-center">
      <Alert view="danger" :message="MESSAGES.NO_COACHES" />
    </div>
  </div>
</template>
