<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import { ref } from "vue";
import Footer from "../components/Footer.vue";
import axios from "axios";
import { useToast } from "vue-toastification";
import { FwbButton } from "flowbite-vue";
import { FwbInput } from "flowbite-vue";

const toast = useToast();
const subscription = ref<string>("");

const sendSubscription = async () => {
  try {
    await axios.post("/api/workout/subscribe/", {
      email: subscription.value
    });
    toast.success("Вы подписались на рассылку");
    subscription.value = "";
  } catch (err: any) {
    toast.error(err.message);
    subscription.value = "";
  }
};
</script>
<template>
  <div class="px-6 sm:mt-20 lg:px-8">
    <div class="relative isolate overflow-hidden px-6 py-24 sm:px-24 xl:py-32">
      <h2
        class="mx-auto max-w-2xl text-center text-3xl font-bold tracking-tight text-white sm:text-4xl"
      >
        Будьте в курсе событий
      </h2>

      <p
        class="mx-auto mt-2 max-w-xl text-center text-lg leading-8 text-gray-300"
      >
        Присоединяйтесь к нашей рассылке для получения выборочных, заслуживающих
        внимания обновлений.
      </p>

      <form
        @submit.prevent="sendSubscription"
        class="mx-auto mt-5 flex justify-center max-w-md gap-x-4"
      >
        <fwb-input type="email" v-model="subscription" required placeholder="Введите почту" />
        <fwb-button size="sm" color="light">Подписаться</fwb-button>
      </form>

      <Footer />
    </div>
  </div>
</template>