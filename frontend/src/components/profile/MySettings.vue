<script setup lang="ts">
defineProps({
    user: Object
})
</script>

<template>
    <div class="flex  text-white">
        <p >{{ user.username }}</p>
        <p>{{ user.email }}</p>
    </div>
</template>

<style scoped></style>