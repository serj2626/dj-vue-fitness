<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>

<template>
  <div class="container row-2xl">
    <section id="loginID"
      class="w-6/12 mx-auto mt-[280px] bg-transparent dark:bg-gray-900 rounded-2xl
     "
    >
      <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
        <h1
        id="login-title"
          class="text-xl font-bold leading-tight tracking-tight
           text-white text-center md:text-2xl dark:text-white"
        >
          Войдите в аккаунт
        </h1>
        <form class="space-y-4 md:space-y-6" action="#">
          <div id="login-email">
            <label
              for="email"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Ваша почта</label
            >
            <input
              type="email"
              name="email"
              id="email"
              class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="name@company.com"
              required
            />
          </div>
          <div id="login-password">
            <label
              for="password"
              class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
              >Пароль</label
            >
            <input
              type="password"
              name="password"
              id="password"
              placeholder="••••••••"
              class="bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              required
            />
          </div>
          <button
            type="submit"
            id="login-button"
            class="form-btn"
          >
            Войти
          </button>
          <p id="login-help" class="text-sm font-light text-yellow-500 dark:text-gray-400">
            У вас нет аккаунта?
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

#login-title{
  animation: show-title .5s ease-in;
}
#login-email{
  animation: show-email .5s ease-in;
}
#login-password{
  animation: show-password .5s ease-in;
}
#login-button{
  animation: show-button .5s ease-in;
}

#login-help{
  animation: show-help ease-in 1.5s;
}

@keyframes show-help{
  0%{
    opacity: 0;
    scale: .5;
    transform: translateY(150px);
  }
  100%{
    opacity: 1;
  }
}


@keyframes show-email{
  0%{
    opacity: 0;
    transform: translateX(-650px);
  }
  100%{
    opacity: 1;
  }
}

@keyframes show-password{
  0%{
    opacity: 0;
    transform: translateX(650px);
  }
  100%{
    opacity: 1;
  }
}


@keyframes show-button{
  0%{
    opacity: 0;
    transform: translateY(150px);
  }
  100%{
    opacity: 1;
  }
}


@keyframes show-title{
  0%{
    opacity: 0;
    transform: translateY(-150px);
  }
  100%{
    opacity: 1;
  }
}

#loginID{
  
  box-shadow: 0 0 25px white,
  0 20px 15px 5px rgba(255, 255, 255, 0.228);
}
</style>
