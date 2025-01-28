<script setup lang="ts">
import { FwbButton } from "flowbite-vue";
import type { IPropsButton } from "@/types/ui";


const { size, color } = defineProps<IPropsButton>();
</script>
<template>
    <fwb-button>
        <slot></slot>
    </fwb-button>
</template>
<style scoped lang="scss"></style>
