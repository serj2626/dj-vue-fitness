<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import type { IReview } from '@/utils/interface';

defineProps({
  reviews: {
    type: Array as () => IReview[],
    default: () => [],
  },
});

</script>


<template>
    <div v-if="reviews.length" class="reviews rounded-lg">
      <div class="reviews__main ">
        <div class="reviews__main-header flex justify-between items-center mb-10 
        fixed top-0 ">
          <h1 class="text-3xl text-center text-white font-extrabold">
            Отзывы
          </h1>
          <a class="block text-red-500 cursor-pointer text-3xl">X</a>
        </div>

        <ul>
          <li 
          v-for="review in reviews" 
          :key="review.id"
          class="reviews-desc flex flex-col gap-6 p-3 rounded-md mb-6">
            <div class="reviews-desc__header flex justify-between items-center">
              <h3>{{ review.user }}</h3>
              <span>{{ review.created_at }}</span>
            </div>
            <div class="reviews-desc__body">
              <p>
                {{ review.text }}.
              </p>
            </div>
          </li>
        </ul>
      </div>
    </div>
</template>

<style scoped>
.reviews-desc {
  background-color: rgb(255, 255, 255);
}


.reviews {
  position: absolute;
  padding: 15px;
  top: 96px;
  right: 0;
  bottom: 0;
  width: 30%;
  background: linear-gradient( 45deg, #a3acac 20%, #a852b7 35%, #227975 100% );
  overflow-y: auto;
  z-index: 100;
}
</style>