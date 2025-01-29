<script setup lang="ts">
import axios from "axios";
import { ref, onMounted, reactive } from "vue";
import { useToast } from "vue-toastification";
import { useRoute, useRouter } from "vue-router";
import { FwbRating, FwbButton } from "flowbite-vue";
import { checkDateOrderTraining } from "@/utils/validators";
import { MESSAGES } from "@/types/messages";
import { AppRoutes } from "@/utils/router";
import Galleria from "primevue/galleria";
import { useCoachStore } from "@/stores/coach";
import { storeToRefs } from "pinia";

const storeCoach = useCoachStore();
const { coach, rates } = storeToRefs(storeCoach);
const { getCoach, getRates, responsiveOptions } = storeCoach;

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
    router.push({ name: AppRoutes.myTrainings });
  } catch (err: any) {
    console.log(err);
    toast.error(err.message);
  }
};

const displayBasic = ref(false);

onMounted(() => {
  getCoach(String(id));
  getRates();
});
</script>

<template>
  <div class="container mt-[100px] rounded-xl shadow-2xl shadow-white">
    <div class="grid grid-cols-2 max-[640px]:grid-cols-1 gap-4 p-5">
      <div
        class="rounded-2xl py-5 px-12 flex flex-col items-center justify-center"
      >
        <img class="rounded-xl" :src="coach.avatar" alt="" />
        <div class="flex flex-col items-center my-10">
          <fwb-rating :rating="coach.total_rating" />
          <div>
            <div class="flex my-5 gap-5 justify-center items-center">
              <div class="flex items-center gap-2 text-white">
                <svg
                  @click="
                    router.push({
                      name: AppRoutes.coachReviews,
                      params: { id: coach.id },
                    })
                  "
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="size-6 cursor-pointer"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M7.5 8.25h9m-9 3H12m-9.75 1.51c0 1.6 1.123 2.994 2.707 3.227 1.129.166 2.27.293 3.423.379.35.026.67.21.865.501L12 21l2.755-4.133a1.14 1.14 0 0 1 .865-.501 48.172 48.172 0 0 0 3.423-.379c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z"
                  />
                </svg>
                <sub class="text-2xl text-yellow-300">{{
                  coach.count_reviews
                }}</sub>
              </div>
              <div class="flex items-center gap-2 text-white">
                <svg
                  @click="displayBasic = true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="size-6 cursor-pointer"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="m2.25 15.75 5.159-5.159a2.25 2.25 0 0 1 3.182 0l5.159 5.159m-1.5-1.5 1.409-1.409a2.25 2.25 0 0 1 3.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 0 0 1.5-1.5V6a1.5 1.5 0 0 0-1.5-1.5H3.75A1.5 1.5 0 0 0 2.25 6v12a1.5 1.5 0 0 0 1.5 1.5Zm10.5-11.25h.008v.008h-.008V8.25Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z"
                  />
                </svg>
                <sub class="text-2xl text-yellow-300">{{
                  coach.images?.length
                }}</sub>
              </div>
            </div>
          </div>
        </div>

        <fwb-button
          @click="showModal = true"
          color="yellow"
          class="block w-full text-lg p-3"
          >Записаться
        </fwb-button>
      </div>

      <div class="text-white py-5 px-12">
        <ul class="coach-info">
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
  </div>
  <Galleria
    v-model:visible="displayBasic"
    :value="coach.images"
    :responsiveOptions="responsiveOptions"
    :numVisible="8"
    containerStyle="width: 50%; w-full"
    :circular="true"
    :fullScreen="true"
    :showItemNavigators="true"
  >
    <template #item="slotProps">
      <img
        :src="slotProps.item.image"
        :alt="slotProps.item.alt"
        style="width: 100%; height: 500px; display: block"
      />
    </template>
    <template #thumbnail="slotProps">
      <img
        :src="slotProps.item.image"
        :alt="slotProps.item.alt"
        style="display: block; height: 60px; width: 100%"
      />
    </template>
  </Galleria>
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

.p-galleria-mask {
    position: fixed;
    background-color: red !important;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
