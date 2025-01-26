<script setup lang="ts">
import { RouterLink, useRouter } from "vue-router";
import { useUserStore } from "@/stores/auth";
import { storeToRefs } from "pinia";
import { useToast } from "vue-toastification";
import { headerLinks } from "@/types/header.data";
import HeaderLink from "./HeaderLink.vue";
import { ref } from "vue";

const showProfile = ref(false);
const closeShowProfile = () => {
  setTimeout(() => {
    showProfile.value = false;
  }, 500);
};

const router = useRouter();

const toast = useToast();
const store = useUserStore();
const { auth } = storeToRefs(store);

const logout = () => {
  store.removeToken();
  router.push({ name: "home" });
  toast.success("Вы вышли из аккаунта");
};
</script>

<template>
  <div
    id="navigation"
    class="header bg-black bg-opacity-50 py-2 fixed z-10 top-0 w-full"
  >
    <div
      class="header__container container-md min-h-20 flex justify-center flex-wrap items-center gap-6"
    >
      <h3 class="header__logo text-yellow-300 font-bold text-lg mr-14">
        <RouterLink :to="{ name: 'home' }">DV FITNESS </RouterLink>
      </h3>
      <div
        class="header__menu flex items-center justify-between flex-wrap gap-4"
      >
        <HeaderLink
          v-for="(link, index) in headerLinks"
          :key="index"
          :link="link"
        />
        <RouterLink
          v-if="!auth.isAuthenticated"
          :to="{ name: 'login' }"
          class="header__link"
          >Войти
        </RouterLink>
        <div
          v-if="auth.isAuthenticated"
          @click="showProfile = true"
          @mouseleave="closeShowProfile"
          class="flex flex-col items-center relative z-50"
        >
          <a class="header__link cursor-pointer">Профиль</a>
          <ul
            :class="showProfile ? 'showDropdownMenu' : 'hidden'"
            class="text-white"
          >
            <RouterLink :to="{ name: 'myAbonements' }">
              <li>Абонементы</li>
            </RouterLink>
            <RouterLink :to="{ name: 'mySettings' }">
              <li>Настройки</li>
            </RouterLink>
            <RouterLink :to="{ name: 'myTrainings' }">
              <li>Тренировки</li>
            </RouterLink>
          </ul>
        </div>
        <a v-if="auth.isAuthenticated" @click="logout()" class="header__link"
          >Выйти</a
        >
        <RouterLink
          :to="{ name: 'abonements' }"
          class="header__link header__link-buy"
          >Купить абонемент</RouterLink
        >
      </div>
    </div>
  </div>
</template>

<style scoped>
.showDropdownMenu {
  position: absolute;
  top: 120%;
  background-color: rgba(0, 0, 0, 0.912);
  border: 2px solid #ffffff;
  border-radius: 10px;
  padding: 15px;
  box-shadow: 0 2px 4px rgba(117, 115, 115, 0.2);
  z-index: 100;

  animation: show-dropdown 0.5s ease-in-out;
}

@keyframes show-dropdown {
  0% {
    opacity: 0;
    scale: 0.5;
    transform: translateY(-150px);
  }

  100% {
    opacity: 1;
  }
}

.showDropdownMenu li {
  margin-bottom: 10px;
  cursor: pointer;
  color: #ffffff;
  transition: all 0.3s ease;

  &:hover {
    color: #fed504;
  }
}

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
