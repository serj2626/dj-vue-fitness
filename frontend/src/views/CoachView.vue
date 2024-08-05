<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";
import { useRoute, useRouter } from "vue-router";
const route = useRoute();

const { id } = route.params;
const toast = useToast();
const coach = ref([]);
const showReviews = ref(false);

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
  <div class="container mt-[220px] flex gap-4 p-9 rounded-xl shadow-2xl shadow-white">
    <div class="w-1/3 mx-auto rounded-2xl flex flex-col items-center justify-center gap-8">
      <img class="" :src="coach.avatar" alt="" />
      <div class="flex items-center">
        <svg class="w-8 h-8 ms-3 text-yellow-300" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
          fill="currentColor" viewBox="0 0 22 20">
          <path
            d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z" />
        </svg>
        <svg class="w-8 h-8 ms-3 text-yellow-300" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
          fill="currentColor" viewBox="0 0 22 20">
          <path
            d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z" />
        </svg>
        <svg class="w-8 h-8 ms-3 text-yellow-300" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
          fill="currentColor" viewBox="0 0 22 20">
          <path
            d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z" />
        </svg>
        <svg class="w-8 h-8 ms-3 text-yellow-300" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
          fill="currentColor" viewBox="0 0 22 20">
          <path
            d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z" />
        </svg>
        <svg class="w-8 h-8 ms-3 text-gray-300 dark:text-gray-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
          fill="currentColor" viewBox="0 0 22 20">
          <path
            d="M20.924 7.625a1.523 1.523 0 0 0-1.238-1.044l-5.051-.734-2.259-4.577a1.534 1.534 0 0 0-2.752 0L7.365 5.847l-5.051.734A1.535 1.535 0 0 0 1.463 9.2l3.656 3.563-.863 5.031a1.532 1.532 0 0 0 2.226 1.616L11 17.033l4.518 2.375a1.534 1.534 0 0 0 2.226-1.617l-.863-5.03L20.537 9.2a1.523 1.523 0 0 0 .387-1.575Z" />
        </svg>
      </div>
      <div>
        <a class="text-white">
          Отзывы <span @click="showReviews = !showReviews" class="text-yellow-500"> (126)</span>
        </a>
      </div>
    </div>

    <div class="w-2/3 text-white">
      <ul class="coach-info">
        <li>{{ coach.first_name }} {{ coach.last_name }}</li>
        <li>{{ coach.position }}</li>
        <li>{{ coach.email }}</li>
        <li>{{ coach.phone }}</li>
        <li>{{ coach.bio }}</li>
      </ul>
    </div>
  </div>
  <transition name="fade">
    <div v-if="showReviews" class="reviews rounded-lg">
      <div class="reviews__main ">
        <div class="reviews__main-header flex justify-between items-center mb-10 
        fixed top-0 ">
          <h1 class="text-3xl text-center text-white font-extrabold">
            Отзывы
          </h1>
          <a class="block text-red-500 cursor-pointer text-3xl">&times</a>
        </div>

        <ul>
          <li class="reviews-desc flex flex-col gap-6 p-3 rounded-md mb-6">
            <div class="reviews-desc__header flex justify-between items-center">
              <h3>{{ coach.first_name }} {{ coach.last_name.at(0) }}</h3>
              <span>10.10.2021</span>
            </div>
            <div class="reviews-desc__body">
              <p>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor
                iste maiores tempora omnis illo mollitia.
              </p>
            </div>
          </li>
          <li class="reviews-desc flex flex-col gap-6 p-3 rounded-md mb-6">
            <div class="reviews-desc__header flex justify-between items-center">
              <h3>{{ coach.first_name }} {{ coach.last_name.at(0) }}</h3>
              <span>10.10.2021</span>
            </div>
            <div class="reviews-desc__body">
              <p>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor
                iste maiores tempora omnis illo mollitia.
              </p>
            </div>
          </li>
          <li class="reviews-desc flex flex-col gap-6 p-3 rounded-md mb-6">
            <div class="reviews-desc__header flex justify-between items-center">
              <h3>{{ coach.first_name }} {{ coach.last_name.at(0) }}</h3>
              <span>10.10.2021</span>
            </div>
            <div class="reviews-desc__body">
              <p>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor
                iste maiores tempora omnis illo mollitia.
              </p>
            </div>
          </li>
          <li class="reviews-desc flex flex-col gap-6 p-3 rounded-md mb-6">
            <div class="reviews-desc__header flex justify-between items-center">
              <h3>{{ coach.first_name }} {{ coach.last_name.at(0) }}</h3>
              <span>10.10.2021</span>
            </div>
            <div class="reviews-desc__body">
              <p>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor
                iste maiores tempora omnis illo mollitia.
              </p>
            </div>
          </li>
          <li class="reviews-desc flex flex-col gap-6 p-3 rounded-md mb-6">
            <div class="reviews-desc__header flex justify-between items-center">
              <h3>{{ coach.first_name }} {{ coach.last_name.at(0) }}</h3>
              <span>10.10.2021</span>
            </div>
            <div class="reviews-desc__body">
              <p>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor
                iste maiores tempora omnis illo mollitia.
              </p>
            </div>
          </li>
          <li class="reviews-desc flex flex-col gap-6 p-3 rounded-md mb-6">
            <div class="reviews-desc__header flex justify-between items-center">
              <h3>{{ coach.first_name }} {{ coach.last_name.at(0) }}</h3>
              <span>10.10.2021</span>
            </div>
            <div class="reviews-desc__body">
              <p>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor
                iste maiores tempora omnis illo mollitia.
              </p>
            </div>
          </li>
          <li class="reviews-desc flex flex-col gap-6 p-3 rounded-md mb-6">
            <div class="reviews-desc__header flex justify-between items-center">
              <h3>{{ coach.first_name }} {{ coach.last_name.at(0) }}</h3>
              <span>10.10.2021</span>
            </div>
            <div class="reviews-desc__body">
              <p>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor
                iste maiores tempora omnis illo mollitia.
              </p>
            </div>
          </li>
          <li class="reviews-desc flex flex-col gap-6 p-3 rounded-md mb-6">
            <div class="reviews-desc__header flex justify-between items-center">
              <h3>{{ coach.first_name }} {{ coach.last_name.at(0) }}</h3>
              <span>10.10.2021</span>
            </div>
            <div class="reviews-desc__body">
              <p>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor
                iste maiores tempora omnis illo mollitia.
              </p>
            </div>
          </li>
          <li class="reviews-desc flex flex-col gap-6 p-3 rounded-md mb-6">
            <div class="reviews-desc__header flex justify-between items-center">
              <h3>{{ coach.first_name }} {{ coach.last_name.at(0) }}</h3>
              <span>10.10.2021</span>
            </div>
            <div class="reviews-desc__body">
              <p>
                Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolor
                iste maiores tempora omnis illo mollitia.
              </p>
            </div>
          </li>
        </ul>
      </div>


    </div>
  </transition>
</template>

<style scoped>
.reviews-desc {
  background-color: rgb(255, 255, 255);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 2.5s linear;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateX(600px);
}



.reviews {
  position: absolute;
  padding: 15px;
  top: 96px;
  right: 0;
  bottom: 0;
  width: 30%;
  background: #1b4543;
  overflow-y: auto;
  z-index: 100;
}

.coach-info li {
  width: 50%;

  border: 2px solid #ffd43b;
  padding: 15px;
  font-size: 18px;
  margin: 20px auto;
  border-radius: 10px;
  list-style: none;
  transition: all 0.3s ease-in;

  &:hover {
    transform: scale(1.1);
  }
}

ul {
  margin: 0;
  padding: 0;
}
</style>
