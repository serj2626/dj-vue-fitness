<script setup lang="ts">
import { useRoute } from "vue-router";
import { computed } from "vue";

const route = useRoute();
let routeName = computed(() => route.name);
import type { IHeaderLink } from "@/types/header.data";

defineProps({
  link: {
    type: Object as () => IHeaderLink,
    required: true,
  },
});
</script>
<template>
  <a v-if="routeName === 'home'" :href="link.link" :class="link.class">
    {{ link.title }}
  </a>
</template>
<style scoped></style>
