<script setup lang="ts">
import axios from "axios";
import { ref, onMounted, reactive, computed } from "vue";
import { useToast } from "vue-toastification";
import CoachCard from "@/components/trainer/CoachCard.vue";
import { FwbInput } from "flowbite-vue";
import { FwbSelect } from "flowbite-vue";
import type { ITrainer, ITrainerInfo } from "@/types/workout";

const trainerInfo = reactive<ITrainerInfo>({
  id: "",
  firstName: "",
  lastName: "",
  position: "",
})


const showDetails = (trainer: ITrainer) => {
  trainerInfo.id = trainer.id;
  trainerInfo.firstName = trainer.first_name;
  trainerInfo.lastName = trainer.last_name;
  trainerInfo.position = trainer.position;
};

const resetDetails = () => {
  trainerInfo.firstName = "";
  trainerInfo.lastName = "";
  trainerInfo.position = "";
  trainerInfo.id = "";
};


const toast = useToast();

const searchName = ref("");
const selected = ref("");
console.log(selected.value);
const categories = [
  { value: "Инструктор бассейна", name: "Инструктор бассейна" },
  { value: "Инструктор тренажерного зала", name: "Инструктор тренажорного зала" },
  { value: "Инструктор йоги", name: "Тренер по йоге" },
];

const coaches = ref<ITrainer[]>([]);
const getCoaches = async () => {
  try {
    const { data } = await axios.get("/api/workout/all-trainers/");
    coaches.value = data;
    console.log(coaches.value);
  } catch (err) {
    toast.error("Произошла ошибка при получении тренеров");
  }
};

const totalCoaches = computed<ITrainer[]>(() => {
  if (selected.value && searchName.value) {
    return coaches.value.filter((coach) => coach.position === selected.value)
      .filter((coach) => coach.first_name.toLowerCase().includes(searchName.value.toLowerCase()) 
      || coach.last_name.toLowerCase().includes(searchName.value.toLowerCase()))
  } else if (selected.value) {
    return coaches.value.filter((coach) => coach.position === selected.value)
  } else {
    if (searchName.value) {
    return coaches.value.filter((coach) => coach.first_name.toLowerCase().includes(searchName.value.toLowerCase()) 
    || coach.last_name.toLowerCase().includes(searchName.value.toLowerCase()))
  }
    return coaches.value
  }
});

onMounted(getCoaches);
</script>

<template>
  <div class="container row my-36">
    <h1 class="text-xl sm:text-2xl md:text-3xl text-center text-uppercase text-yellow-300 mb-12">
      Тренеры
    </h1>
    <div class="flex justify-between items-center">
      <fwb-select
        v-model="selected"
        :options="categories"
        placeholder="Выберите категорию"
        size="sm"
      />

      <fwb-input
        v-model="searchName"
        placeholder="Введите имя тренера"
      >
        <template #prefix>
          <svg
            aria-hidden="true"
            class="w-5 h-5 text-gray-500 dark:text-gray-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
            />
          </svg>
        </template>
      </fwb-input>
    </div>

    <div class="grid max-[450px]:grid-cols-1 grid-cols-2 md:grid-cols-3 gap-10 mt-12 px-3">
      <CoachCard 
        v-for="coach in totalCoaches" 
        :key="coach.id" 
        :coach="coach"
        :currentId="trainerInfo.id"
        @showDetail = "showDetails(coach)"
        @resetData = "resetDetails"  
      />
    </div>
  </div>
</template>