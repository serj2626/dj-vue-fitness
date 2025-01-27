<script setup lang="ts">
import axios from "axios";
import { ref, onMounted, reactive } from "vue";
import { useToast } from "vue-toastification";
import { useRoute, useRouter } from "vue-router";
import { FwbRating } from "flowbite-vue";
import { FwbButton } from "flowbite-vue";
import type { iRate, ITrainer } from "@/types/workout";
import { checkDateOrderTraining } from "@/utils/validators";
import { MESSAGES } from "@/types/messages";
import Icon from "@/components/Icon.vue";
import TrainerImages from "@/components/trainer/TrainerImages.vue";

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
    toast.success(MESSAGES.TRAINING_CREATED);
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



  <div class="container my-[160px] rounded-xl shadow-2xl shadow-white">
    <div class="flex max-[767px]:flex-col gap-4 p-9">
      <div
        class="min-[767px]:w-1/3 mx-auto rounded-2xl flex flex-col items-center justify-center gap-8"
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

      <div class="min-[767px]:w-2/3 text-white">
        <ul class="coach-info">
          <li>
            <div class="flex gap-5">
              <Icon type="user" />
              {{ coach.first_name }} {{ coach.last_name }}
            </div>
          </li>
          <li>
            <div class="flex gap-5">
              <Icon type="position" />
              {{ coach.position }}
            </div>
          </li>
          <li>
            <div class="flex gap-5">
              <Icon type="email" />
              {{ coach.email }}
            </div>
          </li>
          <li>
            <div class="flex gap-5">
              <Icon type="phone" />
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
    <div class="grid grid-cols-3 gap-3 max-[500px]:grid-cols-1 max-[767px]:grid-cols-2">
      <img
        v-for="img in coach.images"
        :key="img.id"
        class="block h-[300px] w-full object-cover"
        :src="img.image"
        alt="photo"
        loading="lazy"
      />
    </div>
    <!-- <div>
      <TrainerImages :images="coach.images" />
    </div> -->
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
<style scoped lang="scss">
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