<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";
import { FwbDropdown } from "flowbite-vue";
import type { IMyAbonement } from "@/types/orders";
import { MESSAGES } from "@/types/messages";
import DeleteModal from "@/components/global/Confirm.vue";
import {
  FwbTable,
  FwbTableBody,
  FwbTableCell,
  FwbTableHead,
  FwbTableHeadCell,
  FwbTableRow,
} from "flowbite-vue";
import { $DelAbonement, $GetMyAbonementsList } from "@/features/order";

const toast = useToast();
const abonemets = ref<IMyAbonement[]>([]);

const selectAbonement = ref<number | null>(null);

const getMyAbonements = async () => {
  try {
    const data = await $GetMyAbonementsList();
    abonemets.value = data;
  } catch {
    toast.error(MESSAGES.DATA_ERROR);
  }
};

const deleteAbonement = async () => {
  try {
    await $DelAbonement(String(selectAbonement.value));
    toast.success(MESSAGES.ABONEMENT_DELETED);
    selectAbonement.value = null;
    getMyAbonements();
  } catch {
    toast.error(MESSAGES.ABONEMENT_DELETED_ERROR);
  }
};

onMounted(() => {
  getMyAbonements();
});
</script>

<template>
  <div v-if="abonemets.length" class="my-36 mx-16 text-center">
    <h1 class="text-3xl text-uppercase text-yellow-300 py-4 mb-10">
      Мои абонементы
    </h1>

    <fwb-table class="min-h-80">
      <fwb-table-head>
        <fwb-table-head-cell>№</fwb-table-head-cell>
        <fwb-table-head-cell>Тариф</fwb-table-head-cell>
        <fwb-table-head-cell>Кол-во месяцев</fwb-table-head-cell>
        <fwb-table-head-cell>Начало</fwb-table-head-cell>
        <fwb-table-head-cell>Конец</fwb-table-head-cell>
        <fwb-table-head-cell>Цена</fwb-table-head-cell>
        <fwb-table-head-cell>Оплачен</fwb-table-head-cell>
        <fwb-table-head-cell></fwb-table-head-cell>
      </fwb-table-head>
      <fwb-table-body>
        <fwb-table-row v-for="(abonement, index) in abonemets" :key="index">
          <fwb-table-cell>{{ index + 1 }}</fwb-table-cell>
          <fwb-table-cell>
            {{ abonement.abonement.title }}
          </fwb-table-cell>
          <fwb-table-cell>{{
            abonement.abonement.number_of_months
          }}</fwb-table-cell>
          <fwb-table-cell>{{ abonement.start }}</fwb-table-cell>
          <fwb-table-cell>{{ abonement.end }}</fwb-table-cell>
          <fwb-table-cell>{{ abonement.abonement.price }}</fwb-table-cell>
          <fwb-table-cell
            ><i class="fa-solid fa-xmark fa-2xl" style="color: #ff0000"></i
          ></fwb-table-cell>
          <fwb-table-cell>
            <fwb-dropdown class="text-center" placement="left" text="Действие">
              <div
                class="w-52 border-2 text-center border-slate-300 rounded-lg shadow-xl shadow-zinc-400"
              >
                <p
                  @click="selectAbonement = abonement.id"
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
  </div>

  <DeleteModal
    @closeModal="selectAbonement = null"
    @delete="deleteAbonement"
    view="abonement"
    v-if="selectAbonement"
  />

  <div v-else class="h-[800px] flex justify-center items-center">
    <Alert view="danger" :message="MESSAGES.NO_ABONEMENTS" />
  </div>
</template>
