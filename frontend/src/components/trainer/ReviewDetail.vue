<script setup lang="ts">
import type { IReview } from '@/interfaces/workout';
import { FwbRating } from 'flowbite-vue'
import Rating from "primevue/rating";
defineProps({
    review: {
        type: Object as () => IReview,
        required: true
    }
})
</script>

<template>
        <div
          class="reviews__desc w-[85%] mx-auto flex flex-col gap-6 p-2 rounded-md my-10"
        >
          <div class="reviews-desc__header flex justify-between items-center">
            <div class="flex gap-3">
              <h3>{{ review.user }}</h3>
              <fwb-rating size="sm"  :rating="review.rating" />
              <!-- <Rating disabled readonly :stars="5" :modelValue="review.rating" /> -->
            </div>
            
            <span>{{ review.created_at }}</span>
          </div>
          <div class="reviews-desc__body">
            <p>{{ review.text }}</p>
          </div>
        </div>
</template>

<style scoped>
.reviews__desc {
  background-color: rgba(102, 93, 93, 0.223);
  color: white;
  box-shadow: 0 0 15px rgb(219, 217, 217);
}

</style>