<script setup lang="ts">
import axios from "axios";

import { useToast } from "vue-toastification";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { FwbDropdown } from "flowbite-vue";
import type { IMyTrainig } from "@/interfaces/orders";

import Paginator from "primevue/paginator";
import DeleteModal from "@/components/DeleteModal.vue";

const router = useRouter();
const toast = useToast();

const trainings = ref<IMyTrainig[]>([]);

const currentPage = ref(1);
const itemsPerPage = ref(5);

const selectTrain = ref(null);

const getMyTrainings = async () => {
  try {
    const { data } = await axios.get("/api/auth/my-trainings/");
    trainings.value = data.results;
    console.log(trainings.value);
  } catch {
    toast.error("Произошла ошибка при получении тренировок");
  }
};

onMounted(() => getMyTrainings());
</script>

<template>
  <div class="my-36 mx-16">
    <h1 class="text-3xl text-center text-uppercase text-yellow-300 py-4 mb-10">
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
            <th scope="col" class="px-6 py-3">№</th>
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
            v-for="(train, index) in trainings"
            :key="train.id"
            class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
          >
            <td class="px-6 py-4">{{ index + 1 }}</td>
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
              <fwb-dropdown placement="left" text="Выбрать">
                <div
                  class="w-52 border-2 border-slate-300 rounded-lg shadow-xl shadow-zinc-400"
                >
                  <p 
                  @click="selectTrain = train"
                  class="p-2 hover:bg-slate-200 cursor-pointer">Удалить</p>
                  <p
                    @click="
                      router.push({
                        name: 'payTraining',
                        params: { id: train.id },
                      })
                    "
                    class="p-2 hover:bg-slate-200 cursor-pointer"
                  >
                    Оплатить
                  </p>
                </div>
              </fwb-dropdown>
            </td>
          </tr>
        </tbody>
      </table>

      <Paginator 
      v-model="currentPage" 
      :rows="itemsPerPage" 
      :totalRecords="trainings.length">
      </Paginator>
    </div>

    <DeleteModal
    :text="`Вы действительно хотите удалить тренировку?`"
    v-if="selectTrain" 
    @closeModal="selectTrain = null" 
    @delete="getMyTrainings" />
  </div>
</template>

<style scoped></style>
