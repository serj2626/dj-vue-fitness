<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { FwbRating } from "flowbite-vue";
import { watchEffect } from 'vue';


const toast = useToast();
const route = useRoute();
const router = useRouter();


const review = ref({});

const getReview = async () => {
    try {
        const res = await axios.get(`/api/workout/reviews/${route.params.id}`);
        console.log(res.data);
        review.value = res.data;
    } catch (err) {
        toast.error('Произошла ошибка при получении отзыва');
    }
}

const deleteReview = async () => {
    try {
        await axios.delete(`/api/workout/reviews/${route.params.id}`);
        toast.success('Отзыв успешно удален');
        router.push({name: 'coachReviews', params: {id: review.value.trainer.id}})
    } catch (err) {
        toast.error('Произошла ошибка при удалении отзыва');
    }
}
watchEffect(getReview);
</script>
<template>
    <div class="container text-white">
        <div class="card px-2 py-3">
            <div class="card__header">
                <h3 class="text-center text-yellow-300 text-2xl">Удалить отзыв</h3>
            </div>
            <div class="card__body my-10">
                <div class="flex justify-between items-center mb-4">
                    <fwb-rating size="sm" :rating="review.rating" />
                    <h3>{{ review.date_age }} назад</h3>
                </div>

                <p class="word-wrap">{{ review.text }}</p>
            </div>
            <div class="card__footer flex justify-center gap-6 items-center py-5">
                <button @click="router.go(-1)"
                    class="bg-slate-400 rounded-lg py-2 px-3 hover:bg-slate-500 transition-all duration-300 ease-in">Отмена</button>
                <button 
                @click="deleteReview()"
                class="bg-red-500 rounded-lg py-2 px-3 hover:bg-red-600 transition-all duration-300 ease-in">
                    Удалить
                </button>
            </div>
        </div>
    </div>
</template>
<style scoped>
.word-wrap {
  word-wrap: break-word;
}

.card {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);


    max-height: 400px;
    width: 500px;
    background-color: #655d5d;
    border-radius: 10px;
    box-shadow: 0 0 15px rgb(219, 217, 217);
    cursor: pointer;
}
</style>