<script setup lang="ts">
import { RouterView } from "vue-router";
import {onMounted} from "vue";
import {useToast} from "vue-toastification";
import { useUserStore } from "./stores/auth";
import  Header from "./components/Header.vue";


const store = useUserStore();
const toast = useToast();

onMounted(() =>{
  try {
    store.initStore();
  } catch (error) {
    toast.error("Произошла ошибка");
  }
})
</script>

<template>
  <header>
    <Header />
  </header>

  <main>
    <RouterView />
  </main>

</template>

<style scoped></style>
