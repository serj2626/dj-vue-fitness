<script setup lang="ts">
import type { IPost } from "@/stores/posts";
import { AppRoutes } from "@/utils/router";
import { useRouter } from "vue-router";

const router = useRouter();
defineProps<{
  post: IPost;
}>();
</script>
<template>
  <li
    @click="
      router.push({ name: AppRoutes.post, params: { category: post.category } })
    "
    class="post text-yellow-300"
  >
    {{ post.category }}
  </li>
</template>
<style scoped lang="scss">
.post {
  display: flex;
  align-items: center;
  flex-direction: column;
  cursor: pointer;
  border-radius: 10px;
  padding: 40px;
  outline: 1px solid;
  box-shadow: 0 0 10px #00000038;
  text-transform: uppercase;
  box-shadow: 0 0 15px 10px rgba(255, 255, 1, 0.286);
  transition: all 0.3s ease-in;

  &:hover {
    box-shadow: 0 0 35px 10px yellow;
  }
}
</style>
