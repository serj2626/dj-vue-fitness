<script setup lang="ts">
import { FwbAlert } from 'flowbite-vue'
type AlertType = "success" | "danger" | "warning" | "info"

defineProps<{
    view: AlertType
    message: string 
}>()
</script>
<template>
    <fwb-alert icon :type="view">
        {{ message.toUpperCase() }}
    </fwb-alert>
</template>