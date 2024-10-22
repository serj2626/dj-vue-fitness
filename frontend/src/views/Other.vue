<script setup lang="ts">
import { reactive, ref, watch } from 'vue';

const placeholder = 'sm'

const obj = reactive({
    count: {
        value: 0
    },
    name: "Serj",
    address: {
        city: "SPB",
        street: "Lenina"
    }
})

watch(() => obj.count, (newVal) => {
    console.log(newVal.value);
},
    {
        deep: true
    })
</script>
<template>
 <AuthCard>
ASDASDASDSAD
 </AuthCard>
</template>
<style scoped></style>