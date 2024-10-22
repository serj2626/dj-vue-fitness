<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";
import { FwbDropdown } from "flowbite-vue";
import type { IMyAbonement } from "@/types/orders";
import Paginator from "primevue/paginator";
import { useRouter } from "vue-router";
import DeleteModal from "@/components/DeleteModal.vue";

const router = useRouter();
const toast = useToast();
const abonemets = ref<IMyAbonement[]>([]);

const selectAbonement = ref(null);



const getMyAbonements = async () => {
  try {
    const { data } = await axios.get("/api/auth/my-abonements/");
    abonemets.value = data;
    console.log(abonemets.value);
  } catch (e) {
    toast.error("Произошла ошибка при получении данных");
  }
};


const deleteAbonement = async (id: number) => {
  try {
    await axios.delete(`/api/auth/my-abonements/${selectAbonement.value}/delete`);
    toast.success("Абонемент удален");
    selectAbonement.value = null;
    getMyAbonements();
  } catch (e) {
    toast.error("Произошла ошибка при удалении абонемента");
  }
};

onMounted(() => {
  getMyAbonements();
});
</script>

<template>
  <div class="my-36 mx-16">
    <h1 class="text-3xl text-center text-uppercase text-yellow-300 py-4 mb-10">
      Мои абонементы
    </h1>

    <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
      <table class="w-full text-center text-sm rtl:text-right text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" class="px-6 py-3">№</th>
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
          <tr v-for="(abonement, index) in abonemets" :key="index"
            class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
            <td class="px-6 py-4">{{ index + 1 }}</td>
            <td class="px-6 py-4">
              <a class="text-blue-600">
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
              <fwb-dropdown v-if="!abonement.status" placement="left" text="Выбрать">
                <div class="w-52 border-2 border-slate-300 rounded-lg shadow-xl shadow-zinc-400">
                  <p @click="selectAbonement = abonement.id" class="p-2 hover:bg-slate-200 cursor-pointer">
                    Удалить
                  </p>
                  <p @click="
                    router.push({
                      name: 'payAbonement',
                      params: { id: abonement.id },
                    })
                    " class="p-2 hover:bg-slate-200 cursor-pointer">
                    Оплатить
                  </p>
                </div>
              </fwb-dropdown>
              <button v-else disabled
                class="block w-full text-white bg-slate-700 font-medium rounded-lg text-sm px-5 py-2.5 text-center">
                Оплачен
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <Paginator :rows="10" :totalRecords="120"></Paginator>
    </div>
  </div>

  <DeleteModal 
  @closeModal="selectAbonement = null" 
  @delete="deleteAbonement" 
  :text="`Вы действительно хотите удалить абонемент?`" 
  v-if="selectAbonement" />
</template>
<style scoped></style>
