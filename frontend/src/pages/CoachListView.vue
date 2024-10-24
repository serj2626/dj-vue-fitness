<script setup lang="ts">
import axios from "axios";
import { ref, onMounted, reactive } from "vue";
import { useToast } from "vue-toastification";
import { useRouter } from "vue-router";
import CoachCard from "@/components/trainer/CoachCard.vue";
import { FwbInput } from "flowbite-vue";
import { FwbSelect } from "flowbite-vue";

interface ITrainer {
  id: number;
  first_name: string;
  last_name: string;
  position: string;
  avatar: string;
}

const trainerInfo = reactive({
  id: 0,
  firstName: "",
  lastName: "",
  position: "",
});

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
};

const router = useRouter();
const toast = useToast();

const name = ref("");
const selected = ref("");
const categories = [
  { value: "bass", name: "Инструктор бассейна" },
  { value: "gym", name: "Инструктор тренажорного зала" },
  { value: "yoga", name: "Тренер по йоге" },
];

const coaches = ref<ITrainer[]>([]);
const getCoaches = async () => {
  try {
    const { data } = await axios.get("/api/workout/all-trainers/");
    coaches.value = data;
    console.log(data);
  } catch (err) {
    toast.error("Произошла ошибка при получении тренеров");
  }
};

onMounted(getCoaches);
</script>

<template>
  <div class="container row my-36">
    <h1 class="text-3xl text-center text-uppercase text-yellow-300 mb-12">
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
        v-model="name"
        label="Search"
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

    <div class="grid grid-cols-3 gap-10 mt-12">
      <div v-for="coach in coaches" :key="coach.id">
        <div
          @mouseenter="showDetails(coach)"
          @mouseleave="resetDetails"
          @click="router.push({ name: 'coach', params: { id: coach.id } })"
          class="card"
        >
          <div
            v-if="trainerInfo.id === coach.id"
            class="card__content font-bold"
          >
            <h3 class="card__title text-2xl">
              {{ coach.first_name }} {{ coach.last_name }}
            </h3>
            <p class="card__text">{{ coach.position }}</p>
          </div>
          <img class="card__img rounded-xl" :src="coach.avatar" alt="" />
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.card {
  position: relative;
  max-height: 400px;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 0 15px rgb(219, 217, 217);
  cursor: pointer;
}

.card__content {
  position: absolute;
  z-index: 10;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: #fff;
}

.card__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: all 0.5s ease-in;

&:hover {
  transform: scale(1.1);
  filter:brightness(0.6);
}
}

</style>
