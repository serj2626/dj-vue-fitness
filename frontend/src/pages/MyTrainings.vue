<script setup lang="ts">
import {
  FwbTable,
  FwbTableBody,
  FwbTableCell,
  FwbTableHead,
  FwbTableHeadCell,
  FwbTableRow,
} from "flowbite-vue";
import { useToast } from "vue-toastification";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { FwbDropdown } from "flowbite-vue";
import type { IMyTrainig } from "@/types/orders";
import { $DelTraining, $GetMyTrainingsList } from "@/features/order";
import { MESSAGES } from "@/types/messages";

const router = useRouter();
const toast = useToast();

const trainings = ref<IMyTrainig[]>([]);

const selectTrain = ref<number | string | undefined>("");

const getMyTrainings = async () => {
  try {
    const data = await $GetMyTrainingsList();
    trainings.value = data.results;
  } catch {
    toast.error(MESSAGES.DATA_ERROR);
  }
};

const deleteTraining = async () => {
  try {
    await $DelTraining(String(selectTrain.value));
    toast.success(MESSAGES.TRAINING_DELETED);
    selectTrain.value = "";
    getMyTrainings();
  } catch {
    toast.error(MESSAGES.TRAINING_DELETED_ERROR);
  }
};

onMounted(() => getMyTrainings());
</script>

<template>
  <div v-if="trainings.length" class="my-36 mx-16">
    <h1 class="text-3xl text-center text-uppercase text-yellow-300 py-4 mb-10">
      Мои тренировки
    </h1>

    <fwb-table class="text-center min-h-80">
      <fwb-table-head>
        <fwb-table-head-cell>№</fwb-table-head-cell>
        <fwb-table-head-cell>Тренер</fwb-table-head-cell>
        <fwb-table-head-cell>Позиция</fwb-table-head-cell>
        <fwb-table-head-cell>Начало</fwb-table-head-cell>
        <fwb-table-head-cell>Конец</fwb-table-head-cell>
        <fwb-table-head-cell>Тариф</fwb-table-head-cell>
        <fwb-table-head-cell>Цена</fwb-table-head-cell>
        <fwb-table-head-cell>Оплачен</fwb-table-head-cell>
        <fwb-table-head-cell></fwb-table-head-cell>
      </fwb-table-head>
      <fwb-table-body>
        <fwb-table-row v-for="(train, index) in trainings" :key="train.id">
          <fwb-table-cell>{{ index + 1 }}</fwb-table-cell>
          <fwb-table-cell
            class="cursor-pointer hover:text-blue-700"
            @click="
              router.push({
                name: 'coach',
                params: { id: train.trainer.id },
              })
            "
          >
            {{ train.trainer.first_name }}
            {{ train.trainer.last_name }}
          </fwb-table-cell>
          <fwb-table-cell>{{ train.trainer.position }}</fwb-table-cell>
          <fwb-table-cell>{{ train.start }}</fwb-table-cell>
          <fwb-table-cell>{{ train.end }}</fwb-table-cell>
          <fwb-table-cell>{{ train.rate.title }}</fwb-table-cell>
          <fwb-table-cell>{{ train.rate.price }} руб</fwb-table-cell>
          <fwb-table-cell
            ><i class="fa-solid fa-xmark fa-2xl" style="color: #ff0000"></i
          ></fwb-table-cell>
          <fwb-table-cell>
            <fwb-dropdown placement="left" text="Действие">
              <div
                class="w-52 border-2 text-center border-slate-300 rounded-lg shadow-xl shadow-zinc-400"
              >
                <p
                  @click="selectTrain = train.id"
                  class="p-2 hover:bg-slate-200 cursor-pointer"
                >
                  Удалить
                </p>
                <p class="p-2 hover:bg-slate-200 cursor-pointer">Оплатить</p>
              </div>
            </fwb-dropdown>
          </fwb-table-cell>
        </fwb-table-row>
      </fwb-table-body>
    </fwb-table>

    <Confirm
      v-if="selectTrain"
      view="training"
      @closeModal="selectTrain = ''"
      @delete="deleteTraining"
    />
  </div>

  <div v-else class="h-[800px] flex justify-center items-center">
    <Alert view="danger" :message="MESSAGES.NO_TRAININGS" />
  </div>
</template>
