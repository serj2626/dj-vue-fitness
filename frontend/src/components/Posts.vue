<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";
import { useRouter } from "vue-router";
import type { IPost } from "@/utils/types";


const router = useRouter();
const toast = useToast();
const posts = ref<IPost[]>([]);

const getPosts = async () => {
  try {
    const { data } = await axios.get("/api/workout/posts/");
    posts.value = data;
  } catch {
    toast.error("Произошла ошибка при получении постов");
  }
};

onMounted(getPosts);
</script>

<template>
  <div class="grid grid-cols-5 gap-5 mt-5">
    <div
      @click="
        router.push({ name: 'post', params: { category: post.category } })
      "
      v-for="(post, index) in posts"
      :key="index"
      class="grid__box post"
      data-post="index"
    >
      {{ post.category }}
    </div>
  </div>
</template>

<style scoped>
[data-post] {
  cursor: pointer;
  animation-name: show-post;
  animation-timing-function: ease-in-out;
  animation-duration: calc(atr(data-post) * 2s);
  animation-fill-mode: forwards;
}

@keyframes show-post {
  0% {
    opacity: 0;
    scale: 0.5;
    border: 1px solid orange;
  }
  50% {
    opacity: 1;
    scale: 1;
    border: 2px solid orange;
  }
  100% {
    opacity: 1;
    scale: 1;
  }
  
}
</style>
