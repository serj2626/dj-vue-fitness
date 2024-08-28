<script lang="ts" setup>
import { ref } from "vue";
import { FwbButton, FwbModal } from "flowbite-vue";
import Rating from "primevue/rating";

import { useToast } from "vue-toastification";

const toast = useToast();
const emit = defineEmits(["sendReview", "closeModal"]);



const createReview = () => {
    if (!form.value.rating || !form.value.text) {
        toast.error("Заполните все поля");
        return;
    }

    emit("sendReview", form.value);

    form.value = {
        rating: null,
        text: null,
    };
};

const form = ref({
    rating: null,
    text: null,
});
</script>

<template>

    <fwb-modal  @close="emit('closeModal')">
        <template #header>
            <div class="flex items-center text-lg">Оставьте свой отзыв</div>
        </template>
        <template #body>
            <form id="formReview" @submit.prevent="createReview"
                class="py-6 px-4 w-full mx-auto flex flex-col items-center gap-5">

                <Rating v-model="form.rating" />


                <textarea class="bg-slate-100 w-full border-0 outline-none p-2 rounded-md" placeholder="Введите отзыв"
                    v-model="form.text"></textarea>

            </form>
        </template>
        <template #footer>
            <div class="flex justify-between">
                <fwb-button @click="emit('closeModal')" class="bg-red-500">
                    Отменить
                </fwb-button>
                <fwb-button form="formReview" type="submit" 
                    color="green">Отправить</fwb-button>
            </div>
        </template>
    </fwb-modal>
</template>
