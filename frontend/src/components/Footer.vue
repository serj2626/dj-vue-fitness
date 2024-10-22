<script setup lang="ts">
import { footerLinks } from "@/types/footer.data";
</script>
<template>
  <div
    class="w-[50%] mx-auto flex justify-between items-center h-16 absolute 
    bottom-0 left-[50%] translate-x-[-50%]"
  >
    <div class="text-white">
      <a class="text-yellow-500" href="https://github.com/serj2626"
        >Бойцов Сергей</a
      >
      <p>© 2024 Санкт-Петербург</p>
    </div>
    <ul class="flex items-center gap-2">
      <li
        v-for="(link, index) in footerLinks"
        :key="index"
        class="ms-3 footer-link"
      >
        <a class="text-white" :href="link.link" :title="link.title">
          <i :class="link.icon" :style="link.style"></i
        ></a>
      </li>
    </ul>
  </div>
</template>