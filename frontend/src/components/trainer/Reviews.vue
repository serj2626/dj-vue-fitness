<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import type { IReview } from "@/utils/workout";
import { defineEmits } from "vue";
import ReviewDetail from "@/components/trainer/ReviewDetail.vue";
import Stars from "./Stars.vue";

const emit = defineEmits(["closeModal"]);

defineProps({
  reviews: {
    type: Array as () => IReview[],
    default: () => [],
  },
});
</script>

<template>
  <div class="reviews rounded-lg">
    <div v-if="reviews.length" class="reviews__main">
      <div class="reviews__header flex justify-between items-center mb-10">
        <h4 class="text-2xl text-center text-white font-extrabold">Отзывы</h4>
        <a
          @click="emit('closeModal')"
          class="text-3xl text-white hover:text-red-700 cursor-pointer"
          >&times;</a
        >
      </div>

      <div>
        <form>
          <Stars />
          <div
            class="flex items-center "
          >
            <textarea
              id="chat"
              rows="1"
              class="block mx-4 p-2.5 w-full text-sm text-gray-900 bg-white rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-800 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Ваш отзыв..."
            ></textarea>
            <button
              type="submit"
              class="inline-flex justify-center p-2 text-blue-600 rounded-full cursor-pointer hover:bg-blue-100 dark:text-blue-500 dark:hover:bg-gray-600"
            >
              <svg
                class="w-5 h-5 rotate-90 rtl:-rotate-90 text-red-700"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="currentColor"
                viewBox="0 0 18 20"
              >
                <path
                  d="m17.914 18.594-8-18a1 1 0 0 0-1.828 0l-8 18a1 1 0 0 0 1.157 1.376L8 18.281V9a1 1 0 0 1 2 0v9.281l6.758 1.689a1 1 0 0 0 1.156-1.376Z"
                />
              </svg>
            </button>
          </div>
        </form>
      </div>

      <ul class="my-10" v-for="review in reviews" :key="review.id">
        <ReviewDetail :review="review" />
      </ul>
    </div>

    <div v-else>
      <div class="reviews__header flex justify-between items-center mb-10">
        <a @click="emit('closeModal')" class="close-btn">&times;</a>
      </div>
      <div
        class="reviews__no absolute w-full top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col justify-center items-center gap-5"
      >
        <img
          class="w-1/3 mx-auto"
          src="@/assets/icons/anti-smile.png"
          alt="Отзывы отсутствуют"
        />
        <h4 class="text-3xl text-center text-white font-extrabold">
          Отзывы отсутствуют
        </h4>
      </div>
    </div>
  </div>
</template>

<style scoped>
.reviews {
  position: absolute;
  padding: 15px;
  /* top: 96px; */
  top: 0;
  right: 0;
  bottom: 0;
  width: 30%;
  background: linear-gradient(45deg, #da71a4 20%, #a852b7 35%, #227975 100%);
  overflow-y: auto;
  z-index: 100;
}

.reviews__desc {
  background-color: rgb(255, 255, 255);
  box-shadow: 0 0 15px black;
}

.reviews__main {
  position: relative;
}

.close-btn {
  position: fixed;
  top: 20px;
  font-size: 20px;
  right: 30px;
  font-size: 26px;
  color: white;
  cursor: pointer;
  transition: all 0.5s ease;

  &:hover {
    color: red;
  }
}

.reviews__no h4,
.reviews__header h1 {
  text-shadow: 0 0 10px rgb(0, 0, 0);
}
</style>
