<script setup lang="ts">
import type { ITrainer } from "@/stores/coaches";
import { AppRoutes } from "@/utils/router";
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const selected = ref<string>("");

defineProps<{
  coach: ITrainer;
}>();
</script>

<template>
  <div
    class="card"
    @click="router.push({ name: AppRoutes.coach, params: { id: coach.id } })"
    @mouseenter="selected = coach.id"
    @mouseleave="selected = ''"
  >
    <img
      class="card__img rounded-xl"
      :src="coach.avatar"
      :alt="coach.first_name + ' ' + coach.last_name"
    />
    <div v-if="selected === coach.id" class="card__content font-bold">
      <h3 class="card__title text-3xl">
        {{ coach.first_name }} {{ coach.last_name }}
      </h3>
      <p class="card__text">{{ coach.position }}</p>
    </div>
  </div>
</template>

<style scoped>
.card {
  position: relative;
  max-height: 400px;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 0 15px rgb(219, 217, 217);
  cursor: pointer;
}

.card__content {
  position: absolute;
  z-index: 100;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  color: #fff;
}

.card {
  transition: all 0.3s ease-in;

  &:hover {
    transform: scale(1.05);
    filter: brightness(0.9);
  }
}
</style>
