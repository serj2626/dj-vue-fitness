<script setup lang="ts">
import { ref } from 'vue'
import { FwbSelect } from 'flowbite-vue'

const selected = ref('')
const countries = [
  { value: 'us', name: 'United States' },
  { value: 'ca', name: 'Canada' },
  { value: 'fr', name: 'France' },
]
</script>
<template>
    <fwb-select
      v-model="selected"
      :options="countries"
      placeholder="Select"
      size="sm"
    />
  </template>
<style scoped>
 
</style>