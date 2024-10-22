<script setup lang="ts">
import { useRoute } from 'vue-router';



const route = useRoute();
</script>
<template>
<div class="container border-2 border-white rounded-lg text-orange-400">
 {{ route.params.id }}
</div>
</template>
<style scoped>
 
</style>