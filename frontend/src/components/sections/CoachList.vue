<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useToast } from "vue-toastification";
import { Swiper, SwiperSlide } from "swiper/vue";
import { Pagination, Navigation } from "swiper/modules";
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";

const router = useRouter();
const toast = useToast();
const modules = [Pagination, Navigation];

export interface ITrainerList {
  id: number | string;
  avatar: string;
}

const trainers = ref<ITrainerList[]>([]);
const getCoaches = async () => {
  try {
    const { data } = await axios.get("/api/workout/trainers/");
    trainers.value = data;
  } catch {
    toast.error("Произошла ошибка");
  }
};

onMounted(getCoaches);
</script>

<template>
  <section id="coaches" class="coach container-xl text-orange-300 mb-20">
    <h1
      @click="router.push({ name: 'coachList' })"
      class="text-3xl text-center text-uppercase text-yellow-300 my-16 hover:text-yellow-400 cursor-pointer"
    >
      Наши тренеры
    </h1>

    <swiper
      :loop="true"
      :loopFillGroupWithBlank="true"
      :slidesPerView="1"
      :spaceBetween="5"
      :speed="1000"
      :autoplay="{
        delay: 1000,
      }"
      :pagination="{
        clickable: true,
        type: 'bullets',
      }"
      :navigation="{
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      }"
      :breakpoints="{
        '640': {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        '768': {
          slidesPerView: 3,
          spaceBetween: 20,
        },
        '1024': {
          slidesPerView: 4,
          spaceBetween: 20,
        },
      }"
      :modules="modules"
      class="mySwiper coach__list relative p-40"
    >
      <swiper-slide
        @click="router.push({ name: 'coach', params: { id: trainer.id } })"
        v-for="trainer in trainers"
        :key="trainer.id"
      >
        <img :src="trainer.avatar" alt="" />
      </swiper-slide>
      <div class="swiper-btns">
        <button class="swiper-button-prev text-3xl"></button>
        <button class="swiper-button-next"></button>
      </div>
    </swiper>
  </section>
</template>

<style scoped lang="scss">
.swiper-slide {
  width: auto;
  cursor: pointer;
  border-radius: 20px;
  overflow: hidden;
}

.swiper-slide img {
  display: block;
  width: 100%;
  height: 450px;
  object-fit: cover;
}
.swiper-button-prev {
  color: yellow;
}
.swiper-button-next {
  color: yellow;
}

.swiper-pagination-bullet {
}
.swiper-pagination-bullet {
  background-color: red;
  width: 40px;
  height: 40px;
}
</style>
