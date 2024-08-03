<script setup lang="ts">
import { Swiper, SwiperSlide } from "swiper/vue";
import { Pagination } from "swiper/modules";
import "swiper/css";

import "swiper/css/pagination";

const modules = [Pagination];
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
    <swiper-slide>
      <img src="../assets/img/coach/girl.png" alt="" />
    </swiper-slide>
    <swiper-slide>
      <img src="../assets/img/coach/girl2.png" alt="" />
    </swiper-slide>
    <swiper-slide>
      <img src="../assets/img/coach/man.png" alt="" />
    </swiper-slide>
    <swiper-slide>
      <img src="../assets/img/coach/man2.png" alt="" />
    </swiper-slide>
    <swiper-slide>
      <img src="../assets/img/coach/girl.png" alt="" />
    </swiper-slide>
    <swiper-slide>
      <img src="../assets/img/coach/girl2.png" alt="" />
    </swiper-slide>
    <swiper-slide>
      <img src="../assets/img/coach/man.png" alt="" />
    </swiper-slide>
    <swiper-slide>
      <img src="../assets/img/coach/man2.png" alt="" />
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
