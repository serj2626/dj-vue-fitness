<script setup lang="ts">
import { reactive, ref, watch } from 'vue';
import { FwbButton } from 'flowbite-vue'
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


 <fwb-button color="default">Default</fwb-button>
  <fwb-button color="alternative">Alternative</fwb-button>
  <fwb-button color="dark">Dark</fwb-button>
  <fwb-button color="light">Light</fwb-button>
  <fwb-button color="green">Green</fwb-button>
  <fwb-button color="red">Red</fwb-button>
  <fwb-button color="yellow">Yellow</fwb-button>
  <fwb-button color="purple">Purple</fwb-button>
  <fwb-button color="pink">Pink</fwb-button>
</template>
<style scoped></style>