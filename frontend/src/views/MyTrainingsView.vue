<script setup lang="ts">
import axios from "axios";
import { useToast } from "vue-toastification";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import type { IMyTrainig } from "@/interfaces/orders";
import Paginator from "primevue/paginator";
import Dropdown from 'primevue/dropdown';
const selectedCity = ref();
const cities = ref([
  { name: "New York", code: "NY" },
  { name: "Rome", code: "RM" },
  { name: "London", code: "LDN" },
  { name: "Istanbul", code: "IST" },
  { name: "Paris", code: "PRS" },
]);
const router = useRouter();
const toast = useToast();
const trainings = ref<IMyTrainig[]>([]);

const show = ref(null);

const getMyTrainings = async () => {
  try {
    const { data } = await axios.get("/api/auth/my-trainings/");
    trainings.value = data;
    console.log(trainings.value);
  } catch {
    toast.error("Произошла ошибка при получении тренировок");
  }
};

onMounted(() => getMyTrainings());
</script>

<template>
  <div class="m-16">
    <h1 class="text-3xl text-center text-uppercase text-yellow-500 py-4 mb-10">
      Мои тренировки
    </h1>

    <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
      <table
        class="w-full text-center text-sm rtl:text-right text-gray-500 dark:text-gray-400"
      >
        <thead
          class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
        >
          <tr>
            <th scope="col" class="p-4">
              <div class="flex items-center">
                <input
                  id="checkbox-all-search"
                  type="checkbox"
                  class="hidden w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                />
                <label for="checkbox-all-search" class="sr-only"
                  >checkbox</label
                >
              </div>
            </th>
            <th scope="col" class="px-6 py-3">Тренер</th>
            <th scope="col" class="px-6 py-3">Позиция</th>
            <th scope="col" class="px-6 py-3">Начало</th>
            <th scope="col" class="px-6 py-3">Конец</th>
            <th scope="col" class="px-6 py-3">Тариф</th>
            <th scope="col" class="px-6 py-3">Цена</th>
            <th scope="col" class="px-6 py-3">Оплачен</th>
            <th scope="col" class="px-6 py-3">Действие</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="train in trainings"
            :key="train.id"
            class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
          >
            <td class="w-4 p-4">
              <div class="flex items-center">
                <input
                  id="checkbox-table-search-1"
                  type="checkbox"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                />
                <label for="checkbox-table-search-1" class="sr-only"
                  >checkbox</label
                >
              </div>
            </td>
            <td class="px-6 py-4">
              <a
                class="text-blue-600 hover:underline cursor-pointer"
                @click="
                  router.push({
                    name: 'coach',
                    params: { id: train.trainer.id },
                  })
                "
              >
                {{ train.trainer.first_name }} {{ train.trainer.last_name }}
              </a>
            </td>
            <td class="px-6 py-4">{{ train.trainer.position }}</td>
            <td class="px-6 py-4">{{ train.start }}</td>
            <td class="px-6 py-4">{{ train.end }}</td>
            <td class="px-6 py-4">{{ train.rate.title }}</td>
            <td class="px-6 py-4">{{ train.rate.price }} руб</td>
            <td v-if="train.status" class="px-6 py-4">
              <i class="fa-solid fa-check fa-2xl" style="color: #55ed02"></i>
            </td>
            <td v-else class="px-6 py-4">
              <i class="fa-solid fa-xmark fa-2xl" style="color: #ff0000"></i>
            </td>
            <td class="px-6 py-4">
              <div class="card flex justify-content-center">
      <Dropdown v-model="selectedCity" :options="cities" optionLabel="name" placeholder="Select a City" class="w-full md:w-14rem" />
  </div>
            </td>
          </tr>
        </tbody>
      </table>
      <Paginator
        :rows="10"
        :totalRecords="120"
        :rowsPerPageOptions="[10, 20, 30]"
      ></Paginator>
    </div>
  </div>

</template>

<style scoped></style>

