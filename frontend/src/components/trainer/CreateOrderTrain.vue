<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";
import type {iRate} from "@/types/workout";


defineProps({
  id: String,
  firstName: String,
  lastName: String,
  position: String,
});

const date = defineModel("date");
const choiceRate = defineModel("rate");


const toast = useToast();
const rates = ref<iRate[]>([]);
defineEmits(["closeModal", "orderTraining"]);

const getRates = async () => {
  try {
    const res = await axios.get("/api/workout/rates/");
    rates.value = res.data;
  } catch {
    toast.error("Произошла ошибка при получении данных");
  }
};

onMounted(getRates);
</script>

<template>
  <div class="modal">
    <div class="modal-content w-2/3 relative">
      <div
        class="absolute top-[50%] left-[50%] translate-x-[-50%] translate-y-[-50%] bg-white rounded-lg shadow dark:bg-gray-700"
      >
        <div
          class="flex items-center justify-between p-4 md:p-5 border-b rounded-t dark:border-gray-600"
        >
          <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
            {{ firstName + " " + lastName }} - {{ position }}
          </h3>
          <button
            type="button"
            @click="$emit('closeModal')"
            class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
            data-modal-hide="default-modal"
          >
            <svg
              class="w-3 h-3"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 14 14"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"
              />
            </svg>
            <span class="sr-only">Close modal</span>
          </button>
        </div>

        <div class="p-4 md:p-5 space-y-4">
          <label
            for="date"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
            >Выберите дату занятия</label
          >
          <input
          id=date
          v-model="date"
            class="w-full p-2 border border-gray-300 rounded"
            type="datetime-local"
          />
          
          <label
            for="small"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
            >Выберите тариф</label
          >
          <select
            id="small"
            v-model="choiceRate"
            
            class="block w-full p-2 mb-6 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          >
            <option 
            v-for="rate in rates" :key="rate.id"  :value="rate.id">
              {{rate.title}} - {{ rate.count_minutes }} мин по цене {{ rate.price }} рублей
            </option>
          </select>
          <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
            <span class="font-bold text-xl block underline"> </span>
            Вы можете записаться на персональную тренировку. Для записи выберите
            начальную дату занятия,тариф и нажмите кнопку "Записаться".
          </p>
        </div>
        <div
          class="flex items-center p-4 md:p-5 border-t border-gray-200 rounded-b dark:border-gray-600"
        >
          <button
            @click="$emit('orderTraining')"
            data-modal-hide="default-modal"
            type="button"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
          >
            Записаться
          </button>
          <button
            @click="$emit('closeModal')"
            data-modal-hide="default-modal"
            type="button"
            class="py-2.5 px-5 ms-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700"
          >
            Отмена
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
