<script setup lang="ts">
import type { IReview } from '@/interfaces/workout';
import CreateReview from './CreateReview.vue';
import ReviewDetail from './ReviewDetail.vue';

defineProps({
    reviews: {
        type: Array as () => IReview[],
        required: true
    },
    avatar: {
        type: String,
        required: true
    },
    firstName: {
        type: String,
        required: true
    },
    lastName: {
        type: String,
        required: true
    }
})


</script>
<template>
    <div class="modal z-50">
        <button @click="$emit('closeModal')" class="modal__close">&times;</button>
        <div class="modal__content shadow-2xl shadow-white bg-gradient-to-r from-zinc-800 to-black">
            <div class="">
                <img :src="avatar" alt="zzz" class="w-40 h-40 rounded-full mx-auto my-5" />
                <h3 class="text-2xl text-center text-yellow-400 font-extrabold my-5">{{ firstName + " " + lastName }}</h3>
                <CreateReview @sendReview="$emit('sendReview', $event)" />
            </div>
            <div class="overflow-y-auto">
                <h3 class="text-2xl text-center text-yellow-400 font-extrabold my-5">Отзывы ({{ reviews.length }})</h3>
                <div v-for="review in reviews" :key="review.id">
                    <ReviewDetail :review="review" />
                </div>

            </div>
        </div>
    </div>
</template>
<style scoped>
.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.684);
}

.modal__content {
    position: absolute;
    inset: 50%;
    transform: translate(-50%, -50%);
    display: grid;
    grid-template-columns: 2fr 3fr;

    width: 80%;
    height: 70%;
    border-radius: 5px;

}

.modal__close {
    position: absolute;
    top: 20px;
    right: 30px;
    font-size: 1.5rem;
    cursor: pointer;
    color: white;
    font-size: 36px;
    background-color: transparent;
    border: none;
    transition: all 0.3s ease;

    &:hover {
        transform: scale(1.2);
        color: red;
    }
}
</style>