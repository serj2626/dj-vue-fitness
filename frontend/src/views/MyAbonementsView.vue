<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";

import type { IMyAbonement } from "@/interfaces/orders";

import Paginator from "primevue/paginator";
import Dropdown from "primevue/dropdown";

const toast = useToast();
const abonemets = ref<IMyAbonement[]>([]);

const selectAbonement = ref(null);

const choiceAbonement = (abonId: number) => {
  if (selectAbonement.value === abonId) {
    selectAbonement.value = null;
  } else {
    selectAbonement.value = abonId;
  }
};

const deleteAbonement = async (id: number) => {
  try {
    await axios.delete(`/api/auth/my-abonements/${id}/delete`);
    toast.success("Абонемент удален");
    getMyAbonements();
  } catch (e) {
    toast.error("Произошла ошибка при удалении абонемента");
  }
};

const getMyAbonements = async () => {
  try {
    const { data } = await axios.get("/api/auth/my-abonements/");
    abonemets.value = data;
    console.log(abonemets.value);
  } catch (e) {
    toast.error("Произошла ошибка при получении данных");
  }
};

const actions = ref([{ name: "Удалить" }, { name: "Оплатить" }]);
const selectAction = ref(null);
  
onMounted(() => {
  getMyAbonements();
});
</script>

<template>
  <div class="my-36 mx-16">
    <h1 class="text-3xl text-center text-uppercase text-yellow-500 py-4 mb-10">
      Мои абонементы
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
            <th scope="col" class="px-6 py-3">Тариф</th>
            <th scope="col" class="px-6 py-3">Кол-во месяцев</th>
            <th scope="col" class="px-6 py-3">Начало</th>
            <th scope="col" class="px-6 py-3">Конец</th>
            <th scope="col" class="px-6 py-3">Цена</th>

            <th scope="col" class="px-6 py-3">Оплачен</th>
            <th scope="col" class="px-6 py-3">Действие</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(abonement, index) in abonemets"
            :key="index"
            class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
          >
            <td class="w-4 p-4">
              <div class="flex items-center">
                <input
                  @click="choiceAbonement(abonement.id)"
                  :checked="selectAbonement === abonement.id"
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
              <a class="text-blue-600 hover:underline cursor-pointer">
                {{ abonement.abonement.title }}
              </a>
            </td>
            <td class="px-6 py-4">
              {{ abonement.abonement.number_of_months }}
            </td>
            <td class="px-6 py-4">{{ abonement.start }}</td>
            <td class="px-6 py-4">{{ abonement.end }}</td>
            <td class="px-6 py-4">{{ abonement.abonement.price }} Р</td>

            <td v-if="abonement.status" class="px-6 py-4">
              <i class="fa-solid fa-check fa-2xl" style="color: #55ed02"></i>
            </td>
            <td v-else class="px-6 py-4">
              <i class="fa-solid fa-xmark fa-2xl" style="color: #ff0000"></i>
            </td>
            <td class="px-6 py-4">
              <div class="card flex justify-content-center">
                <Dropdown
                  v-model="selectAbonement"
                  :disabled="selectAbonement !== abonement.id || abonement.status"
                  :options="actions"
                  optionLabel="name"
                  placeholder="Выбрать"
                  class="w-full md:w-14rem"
                />
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
