<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts"></script>

<template>
  <h1 class="text-3xl text-center  text-yellow-300  mb-16">
    О клубе
  </h1>
  <div class="flex justify-between gap-6 about">
    <div class="about__desc">
      <h3 class="about__desc-title uppercase mb-4">Добро пожаловать в DV FITNESS.</h3>
      <div class="about__desc-body leading-7">
        Наша цель - здоровье и комфорт.
        Мы помогаем людям достигать своих целей в лучшую сторону. В нашем клубе
        вы можете отдохнуть и улучшить свою физическую форму. Мы предлагаем
        различные программы, которые помогут вам достичь своих целей.
        На нашем сайте вы можете
        ознакомиться с нашими программами. Приобрести абонемент можно на сайте.
        Также вы можете ознакомиться с нашими тренерами. Заказать персональную тренировку.
      </div>
      <ul class=""> На сайте вы можете:
        <li class="">Приобрести абонемент</li>
        <li>Посмотреть инофрмацию о тренерах</li>
        <li>Приобрести персональную тренировку</li>
        <li>Прочитать полезные статьи</li>
        <li>Купить протеиновую продукцию</li>
      </ul>

    </div>
    <img src="@/assets/img/image.jpg" width="600" height="auto" alt="" class="about__img">
  </div>
</template>

<style scoped>
@keyframes reveal {
  0% {
    opacity: 0;
    clip-path: inset(45% 20% 45% 20%);
  }

  50% {
    opacity: 1;
    clip-path: inset(0% 0% 0% 0%);
  }
}

.about__img {
  animation: reveal linear both;
  animation-timeline: view();
}

ul{
  margin-top: 30px;
  margin-inline: 0;
  list-style-type: disc;
  list-style-position: inside;
  margin-bottom: 20px;


}
ul li{
  margin-bottom: 10px;

}
</style>
