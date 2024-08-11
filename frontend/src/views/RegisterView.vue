<script setup lang="ts">
import { reactive } from "vue";
import { RouterLink } from "vue-router";
import { useToast } from "vue-toastification";
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/auth";
import type { IUserRegister } from "@/interfaces/auth";

const store = useUserStore();
const router = useRouter();
const toast = useToast();

const user = reactive<IUserRegister>({
  username: "",
  email: "",
  password: "",
});

const validateData = () => {
  if (user.username === "" || user.email === "" || user.password === "") {
    toast.error("Заполните все поля");
    return false;
  }
  if (user.password.length < 8) {
    toast.error("Пароль должен содержать не менее 8 символов");
    return false;
  } else {
    return true;
  }
};

const register = async () => {
  if (validateData()) {
    try {
      await store.register(user);
      toast.success("Аккаунт создан");
      router.push({ name: "login" });
    } catch (error) {
      toast.error("Пользователь с таким именем или почтой уже существует");
    }
  }
};
</script>

<template>
  <div class="container row-2xl">
    <section
      id="registerID"
      class="w-6/12 mx-auto mt-[180px] bg-transparent dark:bg-gray-900 rounded-2xl"
    >
      <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
        <h1
          id="login-title"
          class="text-xl font-bold leading-tight tracking-tight text-yellow-500 text-center md:text-2xl dark:text-white"
        >
          Создание аккаунта
        </h1>
        <img
          class="mx-auto form-img"
          width="60"
          height="auto"
          src="../assets/icons/fitness.png"
          alt="Fitness"
        />
        <form @submit.prevent="register" class="space-y-4 md:space-y-6">
          <div
            id="login-username"
            class="flex justify-between items-center gap-6"
          >
            <img
              src="../assets/icons/user.png"
              width="40"
              height="40"
              alt="user"
            />
            <input
              v-model="user.username"
              type="text"
              name="username"
              id="username"
              class="bg-gray-50 w-full border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Как вас зовут?"
              required
            />
          </div>

          <div id="login-email" class="flex justify-between items-center gap-6">
            <img
              src="../assets/icons/email.png"
              width="40"
              height="40"
              alt="user"
            />

            <input
              v-model="user.email"
              type="email"
              name="email"
              id="email"
              class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Введите вашу почту"
              required
            />
          </div>
          <div
            id="login-password"
            class="flex justify-between items-center gap-6"
          >
            <img
              src="../assets/icons/password.png"
              width="40"
              height="40"
              alt="user"
            />
            <input
              v-model="user.password"
              type="password"
              name="password"
              id="password"
              placeholder="Ваш пароль"
              class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              required
            />
          </div>
          <div class="flex justify-between items-center">
            <button type="submit" id="login-button" class="form-btn">
              Регистрация
            </button>
            <p
              id="login-help"
              class="text-sm font-bold text-yellow-500 dark:text-gray-400"
            >
              <span class="text-white"> Уже есть аккаунт? </span>
              <RouterLink
                class="font-medium text-primary-600 hover:underline dark:text-primary-500"
                :to="{ name: 'login' }"
                >Войти</RouterLink
              >
            </p>
          </div>
        </form>
      </div>
    </section>
  </div>
</template>

<style>
.form-img {
  animation: show-img 2.5s linear;
}

@keyframes show-img {
  0% {
    opacity: 0;
  }
}

#login-username {
  animation: show-username 0.5s ease-in;
}

#login-email {
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
    transform: translateX(650px);
  }

  100% {
    opacity: 1;
  }
}

@keyframes show-password {
  0% {
    opacity: 0;
    transform: translateX(-650px);
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

@keyframes show-username {
  0% {
    opacity: 0;
    transform: translateX(-650px);
  }

  100% {
    opacity: 1;
  }
}

#registerID {
  box-shadow: 0 0 25px white, 0 20px 15px 5px rgba(255, 255, 255, 0.228);
}
</style>
