<script setup lang="ts">
import type { IReview } from '@/utils/interface';

defineProps({
    review: {
        type: Object as () => IReview,
        required: true
    }
})
</script>

<template>
        <li
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
</template>

<style scoped>
.reviews__desc {
  background-color: rgb(255, 255, 255);
  box-shadow: 0 0 15px black;
}

</style>