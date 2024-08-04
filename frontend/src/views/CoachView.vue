<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";
import { useRoute, useRouter } from "vue-router";
const route = useRoute();

const { id } = route.params;
const toast = useToast();
const coach = ref([]);

const getCoach = async () => {
  try {
    const { data } = await axios.get(`/api/workout/trainers/${id}`);
    console.log(data);
    coach.value = data;
  } catch {
    toast.error("Произошла ошибка при получении тренера");
  }
};

onMounted(getCoach);
</script>

<template>
  <div></div>
</template>

<style scoped></style>
