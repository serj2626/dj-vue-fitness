<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import { Swiper, SwiperSlide } from "swiper/vue";
import { Pagination, Navigation } from "swiper/modules";
import "swiper/css";
import 'swiper/css/pagination';
import 'swiper/css/navigation';
import type { ITrainerList } from "@/interfaces/workout";


const router = useRouter();
const toast = useToast();
const modules = [Pagination , Navigation];




const trainers = ref<ITrainerList[]>([]);
const getCoaches = async () => {
  try {
    const { data } = await axios.get("/api/workout/trainers/");
    trainers.value = data;
    console.log(data);
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
    :loopFillGroupWithBlank="true"
    :slidesPerView="1"
    :spaceBetween="5"
    :pagination="{
      clickable: true,
    }"
    :navigation="true"
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
  --swiper-pagination-color: #fcc707;
  --swiper-pagination-bullet-size: 18px;
  --swiper-pagination-bullet-width: 18px;
  --swiper-pagination-bullet-height: 18px;
  --swiper-pagination-bullet-inactive-color: #3322c9;
  --swiper-pagination-bullet-inactive-opacity: 0.7;
  --swiper-pagination-bullet-opacity: 1;
  --swiper-pagination-bullet-horizontal-gap: 9px;
  --swiper-pagination-bullet-vertical-gap: 6px;

  --swiper-navigation-color: orange;
  --swiper-navigation-size: 100px;

  --swiper-navigation-offset-horizontal: 0;
  --swiper-navigation-offset-vertical: 0;




  width: 100%;
  height: 100%;
}

.swiper-slide {
  margin: 0 50px;
  text-align: center;
  font-size: 18px;
  background: #fff;
  width: auto;
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
