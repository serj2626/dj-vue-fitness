<script setup lang="ts">
import { FwbRating } from "flowbite-vue";
import type { ITrainer } from "@/types/workout";
import axios from "axios";
import { ref, watchEffect } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import ReviewDetail from "@/components/trainer/ReviewDetail.vue";
import CreateReviewForm from "@/components/trainer/CreateReviewForm.vue";
import DeleteModal from "@/components/DeleteModal.vue";

const router = useRouter();
const route = useRoute();

const coach = ref<ITrainer>({} as ITrainer);

const showFormCreateReview = ref(false);
const selectDelReview = ref(null);

const toast = useToast();

interface IForm {
  text: string;
  rating: number;
}

const getCoach = async () => {
  try {
    const { data } = await axios.get(
      `/api/workout/trainers/${route.params.id}`
    );
    console.log(data);
    coach.value = data;
  } catch {
    toast.error("Произошла ошибка при получении тренера");
  }
};

const createReview = async (form: IForm) => {
  try {
    await axios.post("/api/workout/reviews/create", {
      text: form.text,
      trainer: coach.value.id,
      rating: form.rating,
    });
    toast.success("Отзыв успешно создан");
    showFormCreateReview.value = false;
    getCoach();
  } catch (err) {
    console.log(err);
    toast.error("Произошла ошибка при создании отзыва");
  }
};

const deleteReview = async () => {
  try {
    await axios.delete(`/api/workout/reviews/${selectDelReview.value}`);
    toast.success("Отзыв успешно удален");
    selectDelReview.value = null;
    getCoach();
  } catch (err) {
    console.log(err);
    toast.error("Произошла ошибка при удалении отзыва");
  }
};


watchEffect(getCoach);
</script>
<template>
  <div
    class="reviews w-11/12 mt-[120px] mx-auto p-2 rounded-xl shadow-2xl shadow-white"
  >
    <div class="mx-auto rounded-2xl flex flex-col justify-center items-center">
      <img
        class="rounded-xl w-2/3 h-auto mb-10"
        :src="coach.avatar"
        :alt="coach.first_name"
      />
      <fwb-rating :rating="coach.total_rating" />
      <h1 class="text-xl text-center text-white my-2">
        {{ coach.first_name }} {{ coach.last_name }}
      </h1>

      <button
        @click="showFormCreateReview = true"
        class="form-btn w-3/4 mx-auto my-5"
      >
        Добавить отзыв
      </button>

      <button
        @click="router.push({name: 'coach', params: {id: coach.id}})"
        class="block w-3/4 bg-red-700 mx-auto border-2 border-white border-opacity-30 rounded-md py-3 text-white hover:bg-red-800 active:scale-95 transition-all duration-300 ease-in"
      >
        Назад
      </button>

      <CreateReviewForm
        v-if="showFormCreateReview"
        @sendReview="createReview"
        @closeModal="showFormCreateReview = false"
      />

    </div>

    <div class="h-[800px] overflow-y-auto">
      <h3 class="text-2xl text-center text-yellow-300 my-2">
        Отзывы ({{ coach.count_reviews }})
      </h3>
      <div v-for="review in coach.trainer_reviews" :key="review">
        <ReviewDetail
        :review="review"
        />
      </div>
    </div>

    <DeleteModal
      v-if="selectDelReview"
      :text="`Вы действительно хотите удалить отзыв?`"
      @closeModal="selectDelReview = null"
      @delete="deleteReview"
    />
  </div>
</template>
<style scoped>
.reviews {
  display: grid;
  grid-template-columns: 1fr 2fr;
}
</style>
