<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import type { IAbonement } from "@/utils/orders";
import ModalForm from "@/components/ModalForm.vue";


const router = useRouter();
const toast = useToast();
const abonements = ref<IAbonement[]>([]);
const orderDate = ref('')

const showModal = ref<boolean>(false);

const selectAbonement = ref({} as IAbonement);
const choiceAbonement = (abonement: IAbonement) => {
  if (selectAbonement.value.id === abonement.id) {
    selectAbonement.value = {} as IAbonement;
  } else {
    selectAbonement.value = abonement;
  }
};


const buyAbonement = async () => {
  showModal.value = false;
  try {
    await axios.post(`/api/orders/abonements/${selectAbonement.value.id}/buy/`,
      {
        abonement: selectAbonement.value.id,
        start: orderDate.value,
      }
    )
    toast.success("Вы забронировали абонемент");
    router.push({ name: "profile" })
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
  <div class="container row mt-52">
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
            <th scope="col" class="px-6 py-3">Действие</th>
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
            <td class="px-6 py-4">
              <!-- Modal toggle -->
              <button v-if="selectAbonement.id === abonement.id" @click="showModal = true"
              title="Забронировать"
                class="block text-white bg-transparent
               
                 font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                type="button">
                <i class="fa-solid fa-plus fa-2xl" style="color: #ff5900;"></i>
              </button>

              <button v-else disabled
                class="block text-white bg-transparent font-medium rounded-lg text-sm px-5 py-2.5 text-center"
                type="button">
                <i class="fa-solid fa-minus fa-2xl" style="color: #0011ff;"></i>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <ModalForm 
    v-model:date="orderDate"
    :abonement="selectAbonement" 
    v-if="showModal" 
    @closeModal="showModal = false"
    @orderAbonement="buyAbonement"
    />
</template>

<style scoped>
.abonements {
  box-shadow: 0 5px 40px rgb(228, 227, 221);
}
</style>
