<script setup lang="ts">
import type { IPost } from "@/stores/posts";
import { useRouter } from "vue-router";

const router = useRouter();
defineProps<{
  post: IPost;
}>();
</script>
<template>
  <li
    @click="router.push({ name: 'post', params: { category: post.category } })"
    class="post"
  >
    {{ post.category }}
  </li>
</template>
<style scoped lang="scss">
.post {
  display: flex;
  align-items: center;
  margin-top: 100px;
  flex-direction: column;
  cursor: pointer;
  border-radius: 10px;
  padding: 40px;
  outline: 2px solid;
  box-shadow: 0 0 10px #00000038;

  text-transform: uppercase;
  color: orange;
}
</style>
