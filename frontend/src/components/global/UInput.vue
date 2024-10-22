<script lang="ts" setup>
import { ref } from 'vue'
import { FwbInput } from 'flowbite-vue'


const props = defineProps({
    size: String,
    placeholder: String
})

const name = ref('')
</script>
<template>
    <fwb-input
      v-model="name"
      :size="props.size"
      :placeholder="props.placeholder"
    />
  </template>
<style scoped>
 
</style>