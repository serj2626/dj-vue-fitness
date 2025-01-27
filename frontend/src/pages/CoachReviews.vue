<script setup lang="ts">
import { FwbRating, FwbButton } from "flowbite-vue";
import type { ITrainer } from "@/types/workout";
import axios from "axios";
import { ref, watchEffect } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import ReviewDetail from "@/components/trainer/ReviewDetail.vue";
import { validateDateReview } from "@/utils/validators";
import { MESSAGES } from "@/types/messages";

const route = useRoute();
const router = useRouter();

const coach = ref<ITrainer>({} as ITrainer);

const showFormCreateReview = ref(false);

const toast = useToast();

interface IFormReview {
  message: string;
  rating: number | null;
}

const getCoach = async () => {
  try {
    const { data } = await axios.get(
      `/api/workout/trainers/${route.params.id}`
    );
    coach.value = data;
  } catch {
    toast.error("Произошла ошибка при получении тренера");
  }
};

const createReview = async (form: IFormReview) => {
  try {
    validateDateReview(form);
    await axios.post("/api/workout/reviews/create", {
      text: form.message,
      trainer: coach.value.id,
      rating: form.rating,
    });
    toast.success("Отзыв успешно создан");
    showFormCreateReview.value = false;
    getCoach();
  } catch (err: any) {
    console.log(err);
    toast.error(err.message);
  }
};

const deleteReview = async (id: number) => {
  try {
    await axios.delete(`/api/workout/reviews/${id}`);
    toast.success("Отзыв успешно удален");
    getCoach();
  } catch (err) {
    console.log(err);
    toast.error("Произошла ошибка при удалении отзыва");
  }
};

watchEffect(getCoach);
</script>
<template>
  <div class="mt-[100px]">
    <div
      class="grid grid-cols-[1fr_2fr] container-md p-2 rounded-xl shadow-2xl shadow-white"
    >
      <div class="px-8 py-5 mx-auto flex flex-col items-center">
        <img
          class="reviews__coach-img rounded-xl h-auto mb-10"
          :src="coach.avatar"
          :alt="coach.first_name"
        />
        <div
          class="flex flex-col justify-between w-full"
        >
          <div class="flex flex-col items-center text-white">
            <fwb-rating :rating="coach.total_rating" class="mb-5" />
            <h1 class="text-xl text-center text-white mb-2">
              {{ coach.first_name }} {{ coach.last_name }}
            </h1>
            <p class="reviews__coach-position">{{ coach.position }}</p>
          </div>
          <div class="flex flex-col gap-3 mt-10">
            <fwb-button
              gradient="cyan"
              @click="showFormCreateReview = true"
              class="block w-full text-base p-3"
              >Добавить отзыв
            </fwb-button>

            <fwb-button
              @click="router.back()"
              gradient="red"
              class="block w-full text-base p-3"
              >Назад
            </fwb-button>
          </div>
          <CreateOrderModal
            v-if="showFormCreateReview"
            orderType="review"
            @closeModal="showFormCreateReview = false"
            @createReview="createReview"
          />
        </div>
      </div>

      <div
        v-if="coach.count_reviews"
        class="reviews__body h-[800px] px-5 overflow-y-auto"
      >
        <h3 class="text-2xl text-center text-yellow-300 my-2">
          Отзывы ({{ coach.count_reviews }})
        </h3>

        <ReviewDetail
          v-for="review in coach.trainer_reviews"
          :key="review"
          :review="review"
          @deleteReview="deleteReview"
        />
      </div>

      <div v-else class="h-[800px] flex justify-center items-center">
        <Alert view="danger" :message="MESSAGES.NO_REVIEWS" />
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss">

</style>
