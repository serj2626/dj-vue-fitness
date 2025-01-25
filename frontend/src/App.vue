<script setup lang="ts">
import { RouterView } from "vue-router";
import { onBeforeMount } from "vue";
import { useToast } from "vue-toastification";
import { useUserStore } from "./stores/auth";
import Header from "./components/Header.vue";
import axios from "axios";


const store = useUserStore();
const toast = useToast();

onBeforeMount(() => {
  try {
    store.initStore();
    const token = store.auth.access

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  } catch (error) {
    toast.error("Произошла ошибка");
  }
})
</script>

<template>
  <header>
    <Header />
  </header>

  <main class="main">
    <RouterView />
  </main>
</template>