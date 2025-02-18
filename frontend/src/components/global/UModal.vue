<script lang="ts" setup>
import { FwbButton, FwbModal, FwbTextarea } from "flowbite-vue";
import type { ITrainer, iRate } from "@/types/workout";
import type { IAbonement } from "@/types/orders";
import Rating from "primevue/rating";
import { ref } from "vue";

const date = defineModel("date");
const rate = defineModel("rate");

export interface IFormReview {
  message: string;
  rating: number | null;
}

const formReview = ref<IFormReview>({
  message: "",
  rating: null,
});

type OrderType = "training" | "abonement" | "review" | "updateReview";

interface IProps {
  abonement?: IAbonement;
  coach?: ITrainer;
  orderType: OrderType;
  rates?: iRate[];
  text?: string;
}

defineProps<IProps>();

const emit = defineEmits([
  "closeModal",
  "createOrderTraining",
  "crateOrderAbonement",
  "createReview",
  "updateReview",
]);

const createNewReview = async () => {
  emit("createReview", formReview.value);
};
</script>
<template>
  <!-- Бронирование тренировки -->
  <fwb-modal v-if="orderType === 'training'" @close="$emit('closeModal')">
    <template #header>
      <div class="flex items-center text-lg">Бронирование тренировки</div>
    </template>
    <template #body>
      <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
        {{ coach?.first_name + " " + coach?.last_name }} - {{ coach?.position }}
      </h3>
      <label
        for="date"
        class="block my-2 text-sm font-medium text-gray-900 dark:text-white"
      >
        Выберите дату занятия</label
      >
      <input
        id="date"
        v-model="date"
        class="w-full p-2 border border-gray-300 rounded"
        type="datetime-local"
      />

      <label
        for="small"
        class="block my-2 text-sm font-medium text-gray-900 dark:text-white"
      >
        Выберите тариф
      </label>

      <select
        id="small"
        v-model="rate"
        class="block w-full p-2 mb-6 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      >
        <option v-for="rate in rates" :key="rate.id" :value="rate.id">
          {{ rate.title }} - {{ rate.count_minutes }} мин по цене
          {{ rate.price }} рублей
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
        <fwb-button size="lg" @click="$emit('closeModal')" color="red">
          Отмена
        </fwb-button>
        <fwb-button
          size="lg"
          @click="$emit('createOrderTraining')"
          color="green"
        >
          Записаться
        </fwb-button>
      </div>
    </template>
  </fwb-modal>

  <!-- Бронирование абонемента   -->
  <fwb-modal v-if="orderType === 'abonement'" @close="$emit('closeModal')">
    <template #header>
      <div class="flex items-center text-lg">Бронирование абонемента</div>
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
        {{ abonement?.price }} рублей. Для бронирования выберите начальную дату
        занятий и нажмите кнопку "Забронировать".
      </p>
      <input
        v-model="date"
        class="w-full my-3 p-2 border border-gray-300 rounded"
        type="date"
      />
    </template>
    <template #footer>
      <div class="flex justify-between">
        <fwb-button size="lg" @click="$emit('closeModal')" color="red">
          Отмена
        </fwb-button>
        <fwb-button
          size="lg"
          @click="$emit('crateOrderAbonement')"
          color="green"
        >
          Забронировать
        </fwb-button>
      </div>
    </template>
  </fwb-modal>

  <!-- Редактировать свой отзыв -->
  <fwb-modal v-if="orderType === 'updateReview'" @close="$emit('closeModal')">
    <template #header>
      <div class="flex items-center text-lg">Редактировать свой отзыв</div>
    </template>
    <template #body>
      {{ text }}
      <Rating class="mb-6" v-model="formReview.rating" />
      <fwb-textarea
        @input="formReview.message = $event.target.value"
        :value="text"
        :rows="4"
        label=" Ваш отзыв"
      />
    </template>
    <template #footer>
      <div class="flex justify-between">
        <fwb-button size="lg" @click="$emit('closeModal')" color="red">
          Отмена
        </fwb-button>
        <fwb-button size="lg" @click="createNewReview" color="green">
          Отправить
        </fwb-button>
      </div>
    </template>
  </fwb-modal>

  <!-- Новый отзыв -->
  <fwb-modal v-if="orderType === 'review'" @close="$emit('closeModal')">
    <template #header>
      <div class="flex items-center text-lg">Новый отзыв</div>
    </template>
    <template #body>
      <Rating class="mb-6" v-model="formReview.rating" />
      <fwb-textarea
        v-model="formReview.message"
        :rows="4"
        label=" Ваш отзыв"
        placeholder="Напишите отзыв..."
      />
    </template>
    <template #footer>
      <div class="flex justify-between">
        <fwb-button size="lg" @click="$emit('closeModal')" color="red">
          Отмена
        </fwb-button>
        <fwb-button size="lg" @click="createNewReview" color="green">
          Отправить
        </fwb-button>
      </div>
    </template>
  </fwb-modal>
</template>
