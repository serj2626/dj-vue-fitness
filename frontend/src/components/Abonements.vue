<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";

const toast = useToast();
const abonements = ref([]);

const getAbonements = async (): Promise<void> => {
  try {
    const { data } = await axios.get("/api/abonemens/");
    console.log(data);
    abonements.value = data;
  } catch {
    toast.error("Произошла ошибка");
  }
};
onMounted(() => getAbonements());
</script>

<template>
  <h1 class="text-3xl text-center text-uppercase text-yellow-500">
    Абонементы
  </h1>

  <div
    class="flex justify-center items-center gap-10 mt-10 mb-20 text-yellow-500"
  >
    <div
      v-for="abonement in abonements"
      :key="abonement.id"
      class="box flex flex-col gap-2 items-center justify-around"
    >
      <div class="box__title">
        <h3 class="title text-xl uppercase font-bold">{{ abonement.title }}</h3>
      </div>
      <div class="box__body text-center">
        <p class="text-white mb-4">{{ abonement.description }}</p>
        <span class="text-gray-400">{{ abonement.price }} рублей</span>
      </div>
    </div>
    <!-- <div class="box flex flex-col gap-2 items-center justify-center">
      <h3 class="title">Тариф "Стандартный"</h3>
      <p>9 месяцев</p>
      <span>16000 рублей</span>
    </div>
    <div class="box flex flex-col gap-2 items-center justify-center">
      <h3 class="title">Тариф "Премиум"</h3>
      <p>12 месяцев</p>
      <span>20000 рублей</span>
    </div>
    <div class="box flex flex-col gap-2 items-center justify-center">
      <h3 class="title">Тариф "VIP"</h3>
      <p>18 месяцев</p>
      <span>30000 рублей</span>
    </div> -->
  </div>
</template>

<style scoped>
.box {
  width: 300px;
  height: 300px;

  transition: all 0.3s ease-in;
  border-radius: 10px;
  font-size: 18px;
  box-shadow: 0 0 15px rgba(255, 255, 255, 0.918);
  padding: 15px;

  &:hover {
    transform: scale(1.1);
  }
}

.box:nth-child(1) {
  background: linear-gradient(
    45deg,
    rgb(0, 0, 0) 0%,
    rgba(188, 11, 94, 0.917) 50%
  );
}
.box:nth-child(2) {
  background: linear-gradient(
    45deg,
    rgb(4, 4, 4) 5%,
    rgba(255, 177, 31, 0.917) 100%
  );
}

.box:nth-child(3) {
  background: linear-gradient(
    45deg,
    rgb(32, 41, 49) 0%,
    rgba(251, 39, 255, 0.917) 100%
  );
}

.box:nth-child(4) {
  background: linear-gradient(
    45deg,
    rgb(0, 0, 0) 0%,
    rgba(26, 224, 197, 0.917) 100%
  );
}
</style>
