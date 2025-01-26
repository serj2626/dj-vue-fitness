<script setup lang="ts">
import { onMounted } from "vue";
import { useToast } from "vue-toastification";
import { gsap } from "gsap";
import PostCard from "./PostCard.vue";
import { usePostsStore } from "@/stores/posts";
import { storeToRefs } from "pinia";
const toast = useToast();

const store = usePostsStore();
const { posts } = storeToRefs(store);
const { getPosts } = store;

onMounted(getPosts);

const beforeEnter = (el: any) => {
  el.style.opacity = 0;
  el.style.transform = "translateX(-60px)";
};
const enter = (el: any, done: any) => {
  gsap.to(el, {
    opacity: 1,
    x: 0,
    duration: 0.5,
    onComplete: done,
    delay: el.dataset.index * 0.2,
    ease: "bounce.out",
  });
};
const afterEnter = (el: any) => {
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
      <PostCard
        v-for="(post, index) in posts"
        :key="index"
        :post="post"
        :data-index="index"
      />
    </transition-group>
  </div>
</template>
