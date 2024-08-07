<script setup lang="ts">
import { useUserStore } from "@/stores/auth";
import { storeToRefs } from "pinia";

const store = useUserStore();
const { auth: user } = storeToRefs(store);
</script>

<template>
  <div class="container row mt-[150px]">
    <div class="profile w-2/4 mx-auto p-10 
     rounded-xl flex flex-col items-center">
      <img
        src="@/assets/img/profile.png"
        alt="Profile"
        width="100px"
        height="auto"
      />
      <div class="flex items-center gap-2 mt-5">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="size-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z"
          />
        </svg>
        {{ user.username }}
      </div>
      <div class="flex items-center gap-2 mt-5">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="size-6"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25h-15a2.25 2.25 0 0 1-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615a2.25 2.25 0 0 1-2.36 0L3.32 8.91a2.25 2.25 0 0 1-1.07-1.916V6.75"
          />
        </svg>
        {{ user.email }}
      </div>
    </div>
    <div class="actions flex justify-center items-center gap-10 mt-10">
      <button class="action-btn">Настройки</button>
      <button class="action-btn">Абонементы</button>
      <button class="action-btn">Тренировки</button>
    </div>
  </div>
</template>

<style scoped>
.profile{
    background: linear-gradient(45deg, rgb(236, 48, 180) 0%, rgb(0, 255, 221) 100%);
}

img {
  border-radius: 50%;
  border: 3px solid orange;
  padding: 10px;
}

.action-btn {
  color: rgb(255, 255, 255);
  border-radius: 15px;
  background:linear-gradient(45deg, rgb(236, 48, 180) 0%, rgb(0, 255, 221) 100%);
  padding: 15px 20px;
  font-size: 18px;
}
</style>
