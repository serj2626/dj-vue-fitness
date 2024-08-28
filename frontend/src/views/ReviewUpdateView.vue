<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router';
import { useToast } from 'vue-toastification';
import axios from 'axios';
import { ref, watchEffect } from 'vue';
import Rating from "primevue/rating";

const toast = useToast();
const route = useRoute();
const router = useRouter();

const review = ref({});
const rating = ref(null);
const text = ref('');


const getReview = async () => {
    try {
        const res = await axios.get(`/api/workout/reviews/${route.params.id}`);
        console.log(res.data);
        review.value = res.data;
    } catch (err) {
        toast.error('Произошла ошибка при получении отзыва');
    }
}

const updateReview = async () => {
    try {
        await axios.patch(`/api/workout/reviews/${route.params.id}/`, {
            text: text.value,
            rating: rating.value,
            trainer: review.value.trainer
        });
        toast.success('Отзыв успешно обновлен');
        router.push({name: 'coachReviews', params: {id: review.value.trainer.id}})
    } catch (err) {
        toast.error('Произошла ошибка при обновлении отзыва');
    }
}

watchEffect(getReview);
</script>
<template>
    <div class="container text-white">
        <div class="card px-2 py-3">
            <div class="card__header">
                <h3 class="text-center text-yellow-300 text-2xl">Редактировать отзыв</h3>
            </div>
            <div class="card__body my-10">
                <form
                @submit.prevent="updateReview"
                id="formReview"
                class="py-6 px-4 w-full mx-auto flex flex-col items-center gap-5">

                <Rating v-model="rating" />

                <textarea class="bg-slate-100 text-black w-full 
                border-0 outline-none p-2 rounded-md" :placeholder="review.text"
                v-model="text">
                </textarea>

            </form>
            </div>
            <div class="card__footer flex justify-center gap-6 items-center py-5">
                <button @click="router.go(-1)"
                    class="bg-slate-400 rounded-lg py-2 px-3 hover:bg-slate-500 transition-all duration-300 ease-in">Отмена</button>
                <button 
                form="formReview"
                class="bg-green-500 rounded-lg py-2 px-3 hover:bg-green-600 transition-all duration-300 ease-in">
                    Редактировать
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


    min-height: 400px;
    width: 500px;
    background-color: #00000038;
    border-radius: 10px;
    box-shadow: 0 0 15px rgb(219, 217, 217);
    cursor: pointer;
}
</style>