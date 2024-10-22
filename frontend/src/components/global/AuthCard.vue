<script setup lang="ts">
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import { FwbCard } from 'flowbite-vue'
import { ref } from 'vue';
const props = defineProps({
    title: {
        type: String,
        default: "Card title"
    }

})

const name = ref('')
const psw = ref('')
</script>
<template>
    <fwb-card>
        <div class="p-5">
            <slot name="header">
            <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
                {{ props.title }}
            </h5>
            </slot>
            <slot name="body"></slot>
            <slot name="footer"></slot>

            <slot></slot>
            <p class="font-normal text-gray-700 dark:text-gray-400">
                <InputText type="text" v-model="name" />
                <Password v-model="psw" toggleMask />
            </p>
        </div>
    </fwb-card>
</template>
<style scoped></style>