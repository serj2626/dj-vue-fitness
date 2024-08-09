<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";
import type { IAbonement } from "@/utils/orders";

const toast = useToast();
const abonements = ref<IAbonement[]>([]);

const selectAbonement = ref({} as IAbonement);
const choiceAbonement = (abonement: IAbonement) => {
  if (selectAbonement.value.id === abonement.id) {
    selectAbonement.value = {} as IAbonement;
  } else {
    selectAbonement.value = abonement;
  }
};

const orderDate = ref('')
const phone = ref('')

const buyAbonement = async () => {
  try {
    const { data } = await axios.post(`/api/orders/abonements/${selectAbonement.value.id}/buy/`,
      {
        abonement: selectAbonement.value.id,
        start: orderDate.value,
        phone : phone.value
      }
    )
    toast.success("Вы купили абонемент");
    selectAbonement.value = {} as IAbonement;
  } catch {
    toast.error("Произошла ошибка");
  }
};

const getAbonements = async () => {
  try {
    const { data } = await axios.get("/api/orders/abonements/");
    abonements.value = data;
  } catch {
    toast.error("Произошла ошибка");
  }
};

onMounted(() => getAbonements());
</script>

<template>
  <div class="container row mt-44">
    <div class="abonements relative overflow-x-auto sm:rounded-lg">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
        <thead
          class="text-xs text-white border-2 border-opacity-25 border-white uppercase bg-gray-300 bg-transparent dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" class="p-4">
              <div class="hidden">
                <input id="checkbox-all" type="checkbox"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
                <label for="checkbox-all" class="sr-only">checkbox</label>
              </div>
            </th>
            <th scope="col" class="px-6 py-3">Название абонемента</th>
            <th scope="col" class="px-6 py-3">Количество месяцев</th>
            <th scope="col" class="px-6 py-3">Цена</th>
            <th scope="col" class="px-6 py-3">Описание</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="abonement in abonements" :key="abonement.id"
            class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
            <td class="w-4 p-4">
              <div class="flex items-center">
                <input @click="choiceAbonement(abonement)" id="checkbox-table-1" type="checkbox"
                  :checked="selectAbonement.id === abonement.id"
                  class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" />
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
      <div id="buy" v-show="selectAbonement.id">
        <form @submit.prevent="buyAbonement" class=" flex flex-col justify-between w-2/4 mx-auto my-5">
          <div class="flex bg-slate-400">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor" class="size-6">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M10.5 1.5H8.25A2.25 2.25 0 0 0 6 3.75v16.5a2.25 2.25 0 0 0 2.25 2.25h7.5A2.25 2.25 0 0 0 18 20.25V3.75a2.25 2.25 0 0 0-2.25-2.25H13.5m-3 0V3h3V1.5m-3 0h3m-3 18.75h3" />
            </svg>
            <input
            v-model="phone"
            type="text">
          </div>
          <div class="flex bg-slate-400">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor" class="size-6">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 0 1 2.25-2.25h13.5A2.25 2.25 0 0 1 21 7.5v11.25m-18 0A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75m-18 0v-7.5A2.25 2.25 0 0 1 5.25 9h13.5A2.25 2.25 0 0 1 21 11.25v7.5m-9-6h.008v.008H12v-.008ZM12 15h.008v.008H12V15Zm0 2.25h.008v.008H12v-.008ZM9.75 15h.008v.008H9.75V15Zm0 2.25h.008v.008H9.75v-.008ZM7.5 15h.008v.008H7.5V15Zm0 2.25h.008v.008H7.5v-.008Zm6.75-4.5h.008v.008h-.008v-.008Zm0 2.25h.008v.008h-.008V15Zm0 2.25h.008v.008h-.008v-.008Zm2.25-4.5h.008v.008H16.5v-.008Zm0 2.25h.008v.008H16.5V15Z" />
            </svg>
            <input 
            v-model="orderDate"
            type="date" name="" id="">
          </div>
          <button type="submit" class="btn btn-primary">Купить</button>
        </form>
        {{ selectAbonement }}
      </div>
    </div>


  </div>

</template>

<style scoped>
.abonements {
  box-shadow: 0 5px 40px rgb(228, 227, 221);
}
</style>
