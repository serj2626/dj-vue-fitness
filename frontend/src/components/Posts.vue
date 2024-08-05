<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";
import { useRouter } from "vue-router";

const router = useRouter();
const toast = useToast();
const posts = ref([]);

const getPosts = async () => {
  try {
    const res = await axios.get("/api/workout/posts/");
    console.log(res.data);
    posts.value = res.data;
  } catch {
    toast.error("Произошла ошибка при получении постов");
  }
};

onMounted(getPosts);
</script>

<template>
  <div class="grid grid-cols-5 gap-5 mt-16">
    <div 
    @click="router.push({name: 'post', params: {category: post.category}})"
    v-for="post in posts" 
    :key="post.id" 
    class="grid__box">
      {{ post.category }}
    </div>
  </div>
</template>

<style scoped></style>
