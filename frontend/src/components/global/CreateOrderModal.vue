<script lang="ts" setup>
import { ref } from "vue";
import { FwbButton, FwbModal } from "flowbite-vue";
import type { ITrainerInfo, iRate } from "@/types/workout";
import type { IAbonement } from "@/types/orders";


const date = defineModel("date");

type OrderType = "training" | "abonement";

interface IProps {
    abonement?: IAbonement;
    coach?: ITrainerInfo;
    orderType: OrderType;
    rates?: iRate[]
}

defineProps<IProps>();

const isShowModal = ref(false);

function closeModal() {
  isShowModal.value = false;
}
function showModal() {
  isShowModal.value = true;
}

defineEmits(["closeModal", "createOrderTraining", "crateOrderAbonement"]);
</script>
<template>
  <fwb-modal v-if="orderType === 'training'" @close="closeModal">
    <template #header>
      <div class="flex items-center text-lg">Бронирование тренировки</div>
    </template>
    <template #body>
        <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
            {{ coach?.firstName + " " + coach?.lastName }} - {{ coach?.position }}
          </h3>
        <label for="date" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
            Выберите дату занятия</label>
          <input id=date  class="w-full p-2 border border-gray-300 rounded" type="datetime-local" />
          
        <label for="small" class="block my-2 text-sm font-medium text-gray-900 dark:text-white">
            Выберите тариф
        </label>

          <select id="small"
            class="block w-full p-2 mb-6 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            <option v-for="rate in rates" :key="rate.id" :value="rate.id">
              {{ rate.title }} - {{ rate.count_minutes }} мин по цене {{ rate.price }} рублей
            </option>
          </select>
          <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
            <span class="font-bold text-xl block underline"> </span>
            Вы можете записаться на персональную тренировку. Для записи выберите
            начальную дату занятия,тариф и нажмите кнопку "Записаться".
          </p>
    </template>
    <template #footer>
      <div class="flex justify-between">
        <fwb-button @click="closeModal" color="red">
          Отмена
        </fwb-button>
        <fwb-button @click="closeModal" color="green">
            Записаться
        </fwb-button>
      </div>
    </template>
  </fwb-modal>

  <fwb-modal v-if="orderType === 'abonement'" @close="$emit('closeModal')">
    <template #header>
      <div class="flex items-center text-lg">Бронрование абонемента</div>
    </template>
    <template #body>
        <p class="text-base leading-relaxed text-gray-500 dark:text-gray-400">
            <span class="font-bold text-xl block underline">{{
              abonement?.description
            }}</span>
            Тариф {{ abonement?.title }} вы можете забронировать на нашем сайте.
            Данный абонемент включает в себя
            {{ abonement?.number_of_months }} месяцев занятий без ограничения по
            времени. На данный момент его цена составляет
            {{ abonement?.price }} рублей. Для бронирования выберите начальную
            дату занятий и нажмите кнопку "Забронировать".
          </p>
        <input
            v-model="date"
            class="w-full my-3 p-2 border border-gray-300 rounded"
            type="date"
          />
    </template>
    <template #footer>
      <div class="flex justify-between">
        <fwb-button @click="$emit('closeModal')" color="red">
          Отмена
        </fwb-button>
        <fwb-button @click="$emit('crateOrderAbonement')" color="green">
            Забронировать
        </fwb-button>
      </div>
    </template>
  </fwb-modal>
</template>
<style scoped></style>
