<script setup lang="ts">
import type { ITrainer } from "@/types/workout";
import { useRouter } from "vue-router";

const router = useRouter();

defineProps({
    coach: {
        type: Object as () => ITrainer,
        required: true,
    },
    currentId: {
        type: [Number, String],
        required: true,
    }
});

const emit = defineEmits(["showDetail", "resetData"]);

const selectCoach = (coach: ITrainer): void => {
    emit("showDetail", coach);
};

const resetDataCoach = (): void => {
    emit("resetData");
};
</script>

<template>
    <div class="card">
        <img 
            @click="router.push({ name: 'coach', params: { id: coach.id } })" 
            class="card__img rounded-xl"
            :src="coach.avatar" 
            :alt="coach.first_name + ' ' + coach.last_name" 
            @mouseenter="selectCoach(coach)"
            @mouseleave="resetDataCoach" 
        />
        <div
            v-if="currentId === coach.id"
            class="card__content font-bold"
          >
            <h3 class="card__title text-2xl">
              {{ coach.first_name }} {{ coach.last_name }}
            </h3>
            <p class="card__text">{{ coach.position }}</p>
        </div>
        </div>
</template>

<style scoped>
.card {
    position: relative;
    max-height: 400px;
    background-color: #fff;
    border-radius: 20px;
    box-shadow: 0 0 15px rgb(219, 217, 217);
    cursor: pointer;
}

.card__content {
    position: absolute;
    z-index: 100;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    color: #fff;
}

.card__img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: all 0.3s ease-in;

    &:hover {
        transform: scale(1.1);
        filter: brightness(0.6);
    }
}
</style>
