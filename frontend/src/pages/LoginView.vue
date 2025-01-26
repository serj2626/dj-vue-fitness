<script setup lang="ts">
import { reactive } from "vue";
import { RouterLink } from "vue-router";
import { useToast } from "vue-toastification";
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/auth";
import { FwbButton } from "flowbite-vue";

const store = useUserStore();
const router = useRouter();
const toast = useToast();

type UserLogin = {
  username: string;
  password: string;
};

const user = reactive<UserLogin>({
  username: "",
  password: "",
});

const validateForm = () => {
  if (user.username === "" || user.password === "") {
    toast.error("Заполните все поля");
    return false;
  } else {
    return true;
  }
};

const login = async () => {
  if (validateForm()) {
    try {
      await store.login(user);
      router.push({ name: "home" });
      toast.success("Вы вошли в аккаунт");
    } catch (error) {
      console.log(error);
      toast.error("Неверная почта или имя пользователя");
    }
  }
};
</script>

<template>
  <div class="container row-2xl">
    <section
      id="loginID"
      class="w-6/12 mx-auto mt-[180px] bg-transparent dark:bg-gray-900 rounded-2xl"
    >
      <div class="p-10">
        <h1
          id="login-title"
          class="text-xl font-bold leading-tight tracking-tight text-yellow-500 text-center md:text-2xl dark:text-white"
        >
          Войдите в аккаунт
        </h1>
        <img
          class="mx-auto form-img"
          width="60"
          height="auto"
          src="../assets/icons/fitness2.png"
          alt="Fitness"
        />
        <form @submit.prevent="login" class="space-y-4 md:space-y-6">
          <div id="login-text" class="">
            <label
              for="username"
              class="block text-sm font-medium text-gray-900 dark:text-white"
              >Ваша почта</label
            >
            <input
              v-model="user.username"
              type="text"
              name="username"
              id="username"
              class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Ваше имя "
              required
            />
          </div>
          <div id="login-password" class="">
            <label
              for="password"
              class="block text-sm font-medium text-gray-900 dark:text-white"
              >Пароль</label
            >
            <input
              v-model="user.password"
              type="password"
              name="password"
              id="password"
              placeholder="••••••••"
              class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              required
            />
          </div>
          <fwb-button
            type="submit"
            size="lg"
            class="block w-full"
            color="yellow"
            >Войти</fwb-button
          >
          <p
            id="login-help"
            class="text-sm font-bold text-yellow-500 dark:text-gray-400"
          >
            <span class="text-white"> Нет аккаунта? </span>
            <RouterLink
              class="font-medium text-primary-600 hover:underline dark:text-primary-500"
              :to="{ name: 'register' }"
              >Создать</RouterLink
            >
          </p>
        </form>
      </div>
    </section>
  </div>
</template>

<style>
#login-title {
  animation: show-title 0.5s ease-in;
}

#login-text {
  animation: show-email 0.5s ease-in;
}

#login-password {
  animation: show-password 0.5s ease-in;
}

#login-button {
  animation: show-button 0.5s ease-in;
}

#login-help {
  animation: show-help ease-in 1.5s;
}

@keyframes show-help {
  0% {
    opacity: 0;
    scale: 0.5;
    transform: translateY(150px);
  }

  100% {
    opacity: 1;
  }
}

@keyframes show-email {
  0% {
    opacity: 0;
    transform: translateX(-650px);
  }

  100% {
    opacity: 1;
  }
}

@keyframes show-password {
  0% {
    opacity: 0;
    transform: translateX(650px);
  }

  100% {
    opacity: 1;
  }
}

@keyframes show-button {
  0% {
    opacity: 0;
    transform: translateY(150px);
  }

  100% {
    opacity: 1;
  }
}

@keyframes show-title {
  0% {
    opacity: 0;
    transform: translateY(-150px);
  }

  100% {
    opacity: 1;
  }
}

#loginID {
  box-shadow:
    0 0 25px white,
    0 20px 15px 5px rgba(255, 255, 255, 0.228);
}
</style>
