<script setup lang="ts">
import axios from "axios";
import { ref, onMounted, reactive } from "vue";
import { useToast } from "vue-toastification";
import { useRoute, useRouter } from "vue-router";
import { FwbRating } from "flowbite-vue";
import { FwbBreadcrumb, FwbBreadcrumbItem, FwbButton } from "flowbite-vue";
import type { iRate, ITrainer } from "@/types/workout";
import { checkDateOrderTraining } from "@/validators";
import { Messages } from "@/types/messages";

const router = useRouter();
const route = useRoute();
const { id } = route.params;

interface ItrainingData {
  date: string;
  rate: number;
}

const trainingData = reactive<ItrainingData>({} as ItrainingData);

const toast = useToast();

const showModal = ref<boolean>(false);

const coach = ref<ITrainer>({} as ITrainer);

const createOrderTraining = async () => {
  try {
    checkDateOrderTraining(trainingData.date, trainingData.rate);
    await axios.post("/api/orders/trainings/create/order/", {
      start: trainingData.date,
      rate: trainingData.rate,
      trainer: id,
    });
    toast.success(Messages.TRAINING_CREATED);
    showModal.value = false;
    router.push({ name: "myTrainings" });
  } catch (err: any) {
    console.log(err);
    toast.error(err.message);
  }
};

const getCoach = async () => {
  try {
    const { data } = await axios.get(`/api/workout/trainers/${id}`);
    coach.value = data;
    console.log(data);
  } catch {
    toast.error("Произошла ошибка при получении тренера");
  }
};

const rates = ref<iRate[]>([]);

const getRates = async () => {
  try {
    const res = await axios.get("/api/workout/rates/");
    rates.value = res.data;
  } catch {
    toast.error("Произошла ошибка при получении данных");
  }
};

onMounted(() => {
  getCoach();
  getRates();
});
</script>

<template>
  <div class="container mt-[160px] rounded-xl shadow-2xl shadow-white">
    <fwb-breadcrumb class="bg-black border-0 text-white text-3xl" solid>
      <fwb-breadcrumb-item home href="/"> Главная </fwb-breadcrumb-item>
      <fwb-breadcrumb-item href="/coach-list"> Тренеры </fwb-breadcrumb-item>
      <fwb-breadcrumb-item>Тренер </fwb-breadcrumb-item>
    </fwb-breadcrumb>

    <div class="flex gap-4 p-9">
      <div
        class="w-1/3 mx-auto rounded-2xl flex flex-col items-center justify-center gap-8"
      >
        <img class="rounded-xl" :src="coach.avatar" alt="" />
        <fwb-rating :rating="coach.total_rating" />

        <div>
          <a class="text-white cursor-pointer">
            Отзывы
            <span
              @click="
                router.push({ name: 'coachReviews', params: { id: coach.id } })
              "
              class="text-yellow-300 hover:underline"
            >
              ( {{ coach.count_reviews }} )</span
            >
          </a>
        </div>
        <fwb-button
          @click="showModal = true"
          color="yellow"
          class="block w-full text-lg p-3"
          >Записаться
        </fwb-button>
      </div>

      <div class="w-2/3 text-white">
        <ul class="coach-info">
          <li>
            <div class="flex gap-5">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="size-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z"
                />
              </svg>
              {{ coach.first_name }} {{ coach.last_name }}
            </div>
          </li>
          <li>
            <div class="flex gap-5">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="size-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M9 12.75 11.25 15 15 9.75m-3-7.036A11.959 11.959 0 0 1 3.598 6 11.99 11.99 0 0 0 3 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285Z"
                />
              </svg>
              {{ coach.position }}
            </div>
          </li>
          <li>
            <div class="flex gap-5">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="size-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75"
                />
              </svg>
              {{ coach.email }}
            </div>
          </li>
          <li>
            <div class="flex gap-5">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="size-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 0 1-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z"
                />
              </svg>
              {{ coach.phone }}
            </div>
          </li>
          <li>
            <div class="">
              {{ coach.bio ? coach.bio : "Нет описания" }}
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>

  <CreateOrderModal
    v-if="showModal"
    v-model:date="trainingData.date"
    v-model:rate="trainingData.rate"
    orderType="training"
    @closeModal="showModal = false"
    @createOrderTraining="createOrderTraining"
    :coach="coach"
    :rates="rates"
  />
</template>
<style scoped>
/* Show Reviews Animation */
.fade-enter-active,
.fade-leave-active {
  transition: all 0.3s linear;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateX(500px);
}

.coach-info li {
  width: 50%;
  background-color: rgb(35, 31, 31);
  border: none;
  box-shadow: 0 0 15px white;
  padding: 15px;
  font-size: 18px;
  margin: 25px auto;
  border-radius: 10px;
  list-style: none;
  transition: all 0.3s ease-in;

  &:hover {
    box-shadow: 0 0 25px white;
  }
}

ul {
  margin: 0;
  padding: 0;
}
</style>
