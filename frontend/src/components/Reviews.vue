<script setup lang="ts"></script>


<template>
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
</style>