<script setup lang="ts">
import { RouterLink } from "vue-router";
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";

const toast = useToast();
const abonements = ref([]);


const selectAbonement = ref(null);

const getAbonements = async (): Promise<void> => {
  try {
    const { data } = await axios.get("/api/orders/abonements/");
    console.log(data);
    abonements.value = data;
  } catch {
    toast.error("Произошла ошибка");
  }
};
onMounted(() => getAbonements());
</script>

<template>
  <div class="container row-3xl">



    <div class="abonements relative overflow-x-auto  sm:rounded-lg">
      <table class="w-full text-sm text-left rtl:text-right 
      text-gray-500 dark:text-gray-400">
        <thead
          class="text-xs
          text-white border-2 border-opacity-25 border-white uppercase bg-gray-300 bg-transparent dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" class="p-4">
              <div class="hidden">
                <input id="checkbox-all" type="checkbox"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                <label for="checkbox-all" class="sr-only">checkbox</label>
              </div>
            </th>
            <th scope="col" class="px-6 py-3">
              Название абонемента
            </th>
            <th scope="col" class="px-6 py-3">
              Количество месяцев
            </th>
            <th scope="col" class="px-6 py-3">
              Цена
            </th>
            <th scope="col" class="px-6 py-3">
              Описание
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="abonement in abonements" :key="abonement.id"
            class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
            <td class="w-4 p-4">
              <div class="flex items-center">
                <input v-model="selectAbonement" id="checkbox-table-1" type="checkbox"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                <label for="checkbox-table-1" class="sr-only">checkbox</label>
              </div>
            </td>
            <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
              {{ abonement.title }}
            </th>
            <td class="px-6 py-4">
              {{ abonement.number_of_months }}
            </td>
            <td class="px-6 py-4">
              {{ abonement.price }}
            </td>
            <td class="px-6 py-4">
              {{ abonement.description }}
            </td>

          </tr>
        </tbody>
      </table>
    </div>

    <div id="buy" v-if="selectAbonement">

      {{ selectAbonement }}
    </div>
  </div>
</template>

<style scoped>
.abonements {
  box-shadow: 0 5px 40px rgb(239, 224, 136);
}
</style>
