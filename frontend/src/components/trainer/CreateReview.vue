<script setup lang="ts">

import { ref } from 'vue';


const text = ref("");
const rating = ref(0);
</script>

<template>
    <div>
        <form class="w-3/4 mx-auto bg-purple-300">
            <textarea v-model="text">
        </textarea>
        </form>
    </div>
</template>


<style scoped></style>