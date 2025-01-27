<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";
import { useRoute } from "vue-router";

interface IPost {
  id: number;
  title: string;
  content: string;
  created_at: string;
  updated_at: string;
  category: string;
}

const route = useRoute();
const { category } = route.params;
const toast = useToast();
const post = ref<IPost>({} as IPost);

const getPost = async () => {
  try {
    const res = await axios.get(`/api/workout/posts/${category}`);
    console.log(res.data);
    post.value = res.data;
  } catch {
    toast.error("Произошла ошибка при получении постов");
  }
};

onMounted(getPost);
</script>

<template>
  <ArrowUpButton />
  <div class="container-md rounded-xl bg-white p-12 mt-[100px]">
    <h1 class="text-center mt-5 mb-20 uppercase font-bold">{{ post.title }}</h1>
    <p v-html="post.content"></p>
  </div>
</template>

<style scoped></style>
