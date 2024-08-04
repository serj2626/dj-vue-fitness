<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import { Swiper, SwiperSlide } from "swiper/vue";
import { Pagination } from "swiper/modules";
import "swiper/css";

import "swiper/css/pagination";


const router = useRouter();
const toast = useToast();
const modules = [Pagination];

const trainers = ref([]);
const getCoaches = async () => {
  try {
    const { data } = await axios.get("/api/workout/trainers/");
    console.log(data);
    trainers.value = data;
  } catch {
    toast.error("Произошла ошибка");
  }
};

onMounted(getCoaches);
</script>

<template>
  <h1 class="text-3xl text-center text-uppercase text-yellow-500 my-16">
    Наши тренеры
  </h1>

  <swiper
    :loop="true"
    :slidesPerView="1"
    :spaceBetween="10"
    :pagination="{
      clickable: true,
    }"
    :breakpoints="{
      '640': {
        slidesPerView: 2,
        spaceBetween: 20,
      },
      '768': {
        slidesPerView: 3,
        spaceBetween: 40,
      },
      '1024': {
        slidesPerView: 3,
        spaceBetween: 50,
      },
    }"
    :modules="modules"
    class="mySwiper"
  >
    <swiper-slide 
    @click="router.push({ name: 'coach', params: { id: trainer.id } })"
    v-for="trainer in trainers" :key="trainer.id">
      <img :src="trainer.avatar" alt="" />
    </swiper-slide>
  </swiper>
</template>

<style scoped>
.swiper {
  width: 100%;
  height: 100%;
}

.swiper-slide {
  text-align: center;
  font-size: 18px;
  background: #fff;
  cursor: pointer;

  /* Center slide text vertically */
  display: flex;
  justify-content: center;
  align-items: center;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 400px;
  object-fit: cover;
}
</style>
