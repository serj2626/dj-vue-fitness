<script setup lang="ts">
import axios from "axios";
import { ref, onMounted, reactive } from "vue";
import { useToast } from "vue-toastification";
import { useRoute, useRouter } from "vue-router";
import { FwbRating, FwbButton } from "flowbite-vue";
import type { iRate, ITrainer } from "@/types/workout";
import { checkDateOrderTraining } from "@/utils/validators";
import { MESSAGES } from "@/types/messages";
import Icon from "@/components/Icon.vue";
import { AppRoutes } from "@/utils/router";
import Galleria from "primevue/galleria";
import { useCoachesStore } from "@/stores/coaches";
import { storeToRefs } from "pinia";

const store = useCoachesStore();
const { responsiveOptions } = storeToRefs(store);

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

const displayBasic = ref(false);

onMounted(() => {
  getCoach();
  getRates();
});
</script>

<template>
  <!-- asdasdas -->
  <div class="container mt-[100px] rounded-xl shadow-2xl shadow-white">
    <div class="grid grid-cols-2 max-[640px]:grid-cols-1  gap-4 p-5">
      <div
        class="rounded-2xl py-5 px-12 flex flex-col items-center justify-center"
      >
        <img class="rounded-xl" :src="coach.avatar" alt="" />
        <div class="flex flex-col items-center my-10">
          <fwb-rating :rating="coach.total_rating" />

          <div>
            <a class="text-white cursor-pointer mt-3">
              Отзывы
              <span
                @click="
                  router.push({
                    name: AppRoutes.coachReviews,
                    params: { id: coach.id },
                  })
                "
                class="text-yellow-300 hover:underline"
              >
                ( {{ coach.count_reviews }} )</span
              >
            </a>
          </div>
        </div>
        <div class="flex flex-col gap-3 w-full">
          <fwb-button
            @click="showModal = true"
            color="yellow"
            class="block w-full text-lg p-3"
            >Записаться
          </fwb-button>
          <fwb-button
            v-if="coach?.images?.length"
            @click="displayBasic = true"
            color="purple"
            class="block w-full text-lg p-3"
            >Фотографии
          </fwb-button>
        </div>
      </div>

      <div class="text-white py-5 px-12">
        <ul class="coach-info ">
          <li>
            <div class="flex items-center gap-5">
              <Icon type="user" />
              {{ coach.first_name }} {{ coach.last_name }}
            </div>
          </li>
          <li>
            <div class="flex items-center gap-5">
              <Icon type="position" />
              {{ coach.position }}
            </div>
          </li>
          <li>
            <div class="flex items-center gap-5">
              <Icon type="email" />
              {{ coach.email }}
            </div>
          </li>
          <li>
            <div class="flex items-center gap-5">
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
    <!-- <div
      class="grid grid-cols-3 gap-3 max-[500px]:grid-cols-1 max-[767px]:grid-cols-2"
    >
      <img
        v-for="img in coach.images"
        :key="img.id"
        class="block h-[300px] w-full object-cover"
        :src="img.image"
        alt="photo"
        loading="lazy"
      />
    </div> -->

    <Galleria
      v-model:visible="displayBasic"
      :value="coach.images"
      :responsiveOptions="responsiveOptions"
      :numVisible="9"
      containerStyle="max-width: 50%; w-full"
      :circular="true"
      :fullScreen="true"
      :showItemNavigators="true"
    >
      <template #item="slotProps">
        <img
          :src="slotProps.item.image"
          :alt="slotProps.item.alt"
          style="width: 100%; height: 70vh; display: block"
        />
      </template>
      <template #thumbnail="slotProps">
        <img
          :src="slotProps.item.image"
          :alt="slotProps.item.alt"
          style="display: block; height: 200px; width: 100%"
        />
      </template>
    </Galleria>
  </div>

  <UModal
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
  width: 100%;
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
    box-shadow: 0 0 35px 3px white;
  }
}

ul {
  margin: 0;
  padding: 0;
}
</style>
