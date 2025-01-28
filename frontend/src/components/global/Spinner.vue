<script setup lang="ts">
import { FwbSpinner } from 'flowbite-vue'

const props = defineProps({
    size: String,
    color: String
})
</script>
<template>
    <fwb-spinner />
</template>
<style scoped lang="scss"></style>