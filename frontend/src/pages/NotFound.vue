<!-- <script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();
</script>
<template>
    <div class="info text-yellow-200 px-10 py-12">
        <h1 class="text-9xl text-white text-center mb-8">404</h1>
        <h2 class="text-3xl text-center font-extrabold">Страница не найдена</h2>
        <a @click="router.push({ name: 'home' })" class="text-white mt-10 uppercase 
        hover:text-yellow-200">На
            главную</a>
    </div>
</template>
<style scoped>
.info {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;


    background-color: #00000038;
    border-radius: 10px;
    box-shadow: 0 0 15px rgb(219, 217, 217);
    cursor: pointer;
}

h1{
    text-shadow: 0 0 15px rgb(219, 217, 217);
}
</style> -->

<template>
  <div class="card flex justify-center">
    <Galleria
      v-model:visible="displayBasic"
      :value="images"
      :responsiveOptions="responsiveOptions"
      :numVisible="9"
      containerStyle="max-width: 50%"
      :circular="true"
      :fullScreen="true"
      :showItemNavigators="true"
    >
      <template #item="slotProps">
        <img
          :src="slotProps.item"
          :alt="slotProps.item.alt"
          style="width: 100%; display: block"
        />
      </template>
      <template #thumbnail="slotProps">
        <img
          :src="slotProps.item"
          :alt="slotProps.item.alt"
          style="display: block"
        />
      </template>
    </Galleria>

    <Button
      label="Show"
      class="mt-56"
      icon="pi pi-external-link"
      @click="displayBasic = true"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import one from "../assets/img/coach/girl.png"
import two from "../assets/img/coach/girl2.png"
import three from "../assets/img/coach/man.png"
import foue from "../assets/img/coach/man2.png"
import Galleria from "primevue/galleria";
import Button from "primevue/button";

const images = ref([one, two, three, foue]);
const responsiveOptions = ref([
  {
    breakpoint: "1500px",
    numVisible: 5,
  },
  {
    breakpoint: "1024px",
    numVisible: 3,
  },
  {
    breakpoint: "768px",
    numVisible: 2,
  },
  {
    breakpoint: "560px",
    numVisible: 1,
  },
]);
const displayBasic = ref(false);


</script>
