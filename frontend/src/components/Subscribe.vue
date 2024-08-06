<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import { ref } from "vue";
import Footer from "../components/Footer.vue";
import axios from "axios";
import { useToast } from "vue-toastification";

const toast = useToast();
const subscription = ref<string>("");


const sendSubscription = async () => {
  try {
    await axios.post("/api/workout/subscribe/", {
      email: subscription.value,
    });
    toast.success("Вы подписались на рассылку");
    subscription.value = "";
  } catch (err ) {
    let [error]: string = err.response.data.email;
    if (error) toast.error("Вы уже подписаны на рассылку");
    else toast.error("Что-то пошло не так");
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
        class="mx-auto mt-5 flex max-w-md gap-x-4"
      >
        <label for="email-address" class="sr-only">Почта</label>
        <input
          v-model="subscription"
          id="email-address"
          name="email"
          type="email"
          autocomplete="email"
          required
          class="min-w-0 flex-auto rounded-md border-0 bg-white/5 px-3.5 py-2 text-white shadow-sm ring-1 ring-inset ring-white/10 focus:ring-2 focus:ring-inset focus:ring-white sm:text-sm sm:leading-6"
          placeholder="Введите вашу почту"
        />

        <button
          type="submit"
          class="flex-none rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-gray-900 shadow-sm hover:bg-gray-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"
        >
          Подписаться
        </button>
      </form>

      <svg
        viewBox="0 0 1024 1024"
        class="absolute left-1/2 top-1/2 -z-10 h-[64rem] w-[64rem] -translate-x-1/2"
        aria-hidden="true"
      >
        <circle
          cx="512"
          cy="512"
          r="512"
          fill="url(#759c1415-0410-454c-8f7c-9a820de03641)"
          fill-opacity="0.7"
        ></circle>
        <defs>
          <radialGradient
            id="759c1415-0410-454c-8f7c-9a820de03641"
            cx="0"
            cy="0"
            r="1"
            gradientUnits="userSpaceOnUse"
            gradientTransform="translate(512 512) rotate(90) scale(512)"
          >
            <stop stop-color="#7775D6"></stop>
            <stop offset="1" stop-color="#7ED321" stop-opacity="0"></stop>
          </radialGradient>
        </defs>
      </svg>
      <Footer />
    </div>
  </div>
</template>

<style scoped></style>
