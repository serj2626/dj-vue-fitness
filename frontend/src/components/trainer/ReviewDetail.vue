<script setup lang="ts">
import type { IReview } from '@/interfaces/workout';

defineProps({
    review: {
        type: Object as () => IReview,
        required: true
    }
})
</script>

<template>
        <li
          class="reviews__desc flex flex-col gap-6 p-3 rounded-md my-10"
        >
          <div class="reviews-desc__header flex justify-between items-center">
            <h3>{{ review.user }}</h3>
            <span>{{ review.created_at }}</span>
          </div>
          <div class="reviews-desc__body">
            <p>{{ review.text }}.</p>
          </div>
        </li>
</template>

<style scoped>
.reviews__desc {
  background-color: rgb(2, 2, 2);
  color: white;
  box-shadow: 0 0 15px rgb(219, 217, 217);
}

</style>