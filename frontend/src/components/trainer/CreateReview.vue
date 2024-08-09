<script setup lang="ts">

import { ref } from 'vue';
import Stars from './Stars.vue';


const text = ref("");
const rating = ref(0);
</script>

<template>
  <form class="py-6 px-4 w-full mx-auto bg-purple-300 flex flex-col items-center gap-5
         rounded-2xl">
          <Stars />
          <div
            class="flex justify-center items-end w-full "
          >
          <textarea class="w-full border-0 outline-none p-2" placeholder="Введите отзыв" v-model="text"></textarea>
           
            <button
              type="submit"
              class="inline-flex justify-center p-2 text-blue-600 rounded-full cursor-pointer
               hover:bg-blue-100 dark:text-blue-500 dark:hover:bg-gray-600"
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
</template>


<style scoped>
form{
  box-shadow: 0 5px 40px rgb(32, 32, 30);
}
</style>