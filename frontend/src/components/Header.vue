<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import { RouterLink } from "vue-router";
import { useUserStore } from "@/stores/auth";

const store = useUserStore();
</script>

<template>
  <div id="navigation" class="header
   bg-black bg-opacity-50 py-2 fixed z-10 top-0 w-full">
    <div class="header__container container h-20 
      flex justify-center flex-wrap items-center 
      
      gap-6">
      <h3 class="header__logo text-yellow-400 font-bold text-lg mr-14">
        <RouterLink :to="{ name: 'home' }">DV FITNESS </RouterLink>
      </h3>
      <div class="header__menu flex items-center gap-4">
        <a href="#about" class="header__link">О клубе</a>
        <a href="#abonements" class="header__link">Абонементы</a>
        <a href="#coach" class="header__link">Тренеры</a>
        <!-- <a href="#" class="header__link">Расписание</a> -->
        <a href="#contacts" class="header__link">Контакты</a>
        <RouterLink :to="{ name: 'login' }" class="header__link">Войти
        </RouterLink>
        <a @click="store.removeToken()" class="header__link">Выйти</a>

        <RouterLink :to="{ name: 'abonements' }" class="header__link header__link__buy">Купить абонемент</RouterLink>
      </div>
    </div>
  </div>
</template>

<style scoped>
.router-link-exact-active {
  color: rgb(255, 212, 19);
}

#navigation {
  animation: show-nav 0.5s ease-in-out;
}

@keyframes show-nav {
  0% {
    opacity: 0;
    scale: 0.5;
    transform: translateY(-150px);
  }

  100% {
    opacity: 1;
  }

}
</style>