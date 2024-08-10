<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import axios from "axios";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toastification";
import { useRouter } from "vue-router";
import type { IPost } from "@/utils/types";
import { gsap } from "gsap";

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

const beforeEnter = (el) => {
  el.style.opacity = 0;
  el.style.transform = "translateX(-60px)";
};
const enter = (el, done) => {
  gsap.to(el, {
    opacity: 1,
    x: 0,
    duration: 0.5,
    onComplete: done,
    delay: el.dataset.index * 0.2,
    ease: "bounce.out",
  });
};
const afterEnter = (el) => {
  gsap.to(el, {
    opacity: 1,
    duration: 0.5,
  });
};
</script>

<template>
  <div class="contact">
    <transition-group
      @before-enter="beforeEnter"
      @enter="enter"
      @after-enter="afterEnter"
      appear
      class="grid grid-cols-5 gap-5 mt-5"
      name="list"
      tag="ul"
    >
      <li
        class="grid__box post"
        v-for="(post, index) in posts"
        :key="index"
        :data-index="index"
      >
        {{ post.category }}
      </li>
    </transition-group>
  </div>
</template>

<!-- <template>
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
</template> -->

<style scoped>

</style>
