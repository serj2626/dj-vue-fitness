<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import type { IReview } from "@/utils/interface";
import { defineEmits } from "vue";

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
        <h1 class="text-3xl text-center text-white font-extrabold">Отзывы</h1>
        <a @click="emit('closeModal')" class="close-btn">&times;</a>
      </div>

      <ul class="my-10">
        <li
          v-for="review in reviews"
          :key="review.id"
          class="reviews__desc flex flex-col gap-6 p-3 rounded-md mb-6"
        >
          <div class="reviews-desc__header flex justify-between items-center">
            <h3>{{ review.user }}</h3>
            <span>{{ review.created_at }}</span>
          </div>
          <div class="reviews-desc__body">
            <p>{{ review.text }}.</p>
          </div>
        </li>
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
          src="../assets/icons/anti-smile.png"
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
  top: 96px;
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
  position: absolute;
  top: 10px;
  right: 20px;
  font-size: 26px;
  color: white;
  cursor: pointer;
  transition: all 0.5s ease;

  &:hover {
    color: red;
  }
}

.reviews__no h4, .reviews__header h1{
  text-shadow: 0 0 10px rgb(0, 0, 0);
}
</style>
