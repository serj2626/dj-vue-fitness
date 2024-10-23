<script setup lang="ts">
import type { IPost } from "@/types/types";
import { useRouter } from "vue-router";

const router = useRouter();
defineProps({
  post: {
    type: Object as () => IPost,
    required: true,
  },
});
</script>
<template>
  <li
    @click="router.push({ name: 'post', params: { category: post.category } })"
    class="grid__box post"
  >
    {{ post.category }}
  </li>
</template>