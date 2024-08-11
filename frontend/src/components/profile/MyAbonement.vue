<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";
import type { IMyAbonement } from "@/interfaces/orders";

const toast = useToast();
const abonemets = ref<IMyAbonement[]>([]);


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

onMounted(() => {
  getMyAbonements();
});
</script>

<template>
  <h1 class="text-3xl text-center text-uppercase text-yellow-500 py-4 mb-10">
    Мои абонементы
  </h1>
  <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
    <table
      class="text-center w-full text-sm rtl:text-right text-gray-500 dark:text-gray-400"
    >
      <thead
        class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
      >
        <tr>
          <th scope="col" class="px-6 py-3">Тариф</th>
          <th scope="col" class="px-6 py-3">Кол-во месяцев</th>
          <th scope="col" class="px-6 py-3">Цена</th>
          <th scope="col" class="px-6 py-3">Начало</th>
          <th scope="col" class="px-6 py-3">Конец</th>
          <th scope="col" class="px-6 py-3">Статус</th>
          <th scope="col" class="px-6 py-3">Действие</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(abonement, index) in abonemets"
          :key="index"
          class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700"
        >
          <td class="px-6 py-4">{{ abonement.abonement.title }}</td>
          <td class="px-6 py-4">{{ abonement.abonement.number_of_months }}</td>
          <td class="px-6 py-4">{{ abonement.abonement.price }} руб</td>
          <td class="px-6 py-4">{{ abonement.start }}</td>
          <td class="px-6 py-4">{{ abonement.end }}</td>
          <td class="px-6 py-4">
            {{ abonement.status ? "Оплачен" : "Не оплачен" }}
          </td>
          <td v-if="abonement.status" class="px-6 py-4">
            <i class="fa-solid fa-check fa-2xl" style="color: #00d118"></i>
          </td>
          <td v-else>
            <div class="flex justify-center gap-4">
              <i
              @click="deleteAbonement(abonement.id)"
                class="block cursor-pointer fa-solid fa-trash fa-xl text-red-600"
                title="Удалить"
              ></i>
              <i
                class="block cursor-pointer fa-solid fa-dollar-sign fa-xl text-green-500"
                title="Оплатить"
              ></i>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped></style>
