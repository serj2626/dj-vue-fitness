<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useToast } from 'vue-toastification';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();


const { category } = route.params
const toast = useToast();
const post = ref([]);

const getPost = async () => {
    try {
        const res = await axios.get(`/api/workout/posts/${category}`);
        console.log(res.data);
        post.value = res.data;
    } catch {
        toast.error('Произошла ошибка при получении постов');
    }
}

onMounted(getPost);
</script>

<template>
      <ArrowUpButton />
    <div class="container row-2xl rounded-xl bg-white p-5 mb-12">
        <h1 class="text-center mt-5 mb-20 uppercase font-bold">{{ post.title }}</h1>
        <p v-html="post.content"></p>

    </div>

</template>

<style scoped></style>