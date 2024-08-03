<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>

<template>
  <div id="" class="header bg-transparent py-4 fixed z-10 top-0 w-full">
    <div
      class="header__container container h-20 flex justify-center items-center gap-6"
    >
      <h3 class="header__logo text-yellow-400 font-bold text-lg mr-14">
        <RouterLink :to="{ name: 'home' }"> VUE FITNESS </RouterLink>
      </h3>
      <div class="header__menu flex items-center gap-4">
        <a href="#about" class="header__link">О клубе</a>
        <a href="#abonements" class="header__link">Абонементы</a>
        <a href="#coach" class="header__link">Тренеры</a>
        <!-- <a href="#" class="header__link">Расписание</a> -->
        <a href="#contacts" class="header__link">Контакты</a>
        <a href="#" class="header__link">Членство клуба</a>
        <RouterLink :to="{ name: 'login' }" class="header__link">Войти</RouterLink>

        <a href="#" class="header__link header__link__buy">Купить абонемент</a>
      </div>
    </div>
  </div>
</template>
