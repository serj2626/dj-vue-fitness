<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();
</script>
<template>
    <div class="info text-yellow-200 px-10 py-12">
        <h1 class="text-3xl text-center font-extrabold">Страница не найдена</h1>
        <a @click="router.push({ name: 'home' })" class="text-white mt-10 uppercase 
        hover:text-red-500">На
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
</style>