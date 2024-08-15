<script setup lang="ts">
import { ref } from 'vue';
import Rating from 'primevue/rating';

const emit = defineEmits(["sendReview"]);

const createReview = () =>{

  emit("sendReview", rating.value, text.value);
  rating.value = null;
  text.value = '';
}

const rating =ref(null);
const text = ref('');

</script>

<template>
  <form
    @submit.prevent="createReview"
    class="py-6 px-4 w-full mx-auto flex flex-col items-center gap-5"
  >
  <div class="card flex justify-center">
      <Rating v-model="rating" />
  </div>
    <div class="flex justify-center items-start w-full">
      <textarea
        class="w-full border-0 outline-none p-2 rounded-md"
        placeholder="Введите отзыв"
        v-model="text"
      ></textarea>

      <button
        type="submit"
        class="inline-flex justify-center p-2 text-blue-600 rounded-full cursor-pointer hover:scale-125 transition-all duration-200 ease-in"
      >
        <svg
          class="w-5 h-5 rotate-90 rtl:-rotate-90 text-yellow-500 hover:text-yellow-600"
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
</template>

<style scoped>

</style>
