<script setup lang="ts">
import { useRoute } from 'vue-router';
import { StripeCheckout } from '@vue-stripe/vue-stripe';


const route = useRoute();
const { id } = route.params;
</script>
<template>
<div class="container border-2 border-white rounded-lg text-orange-400">
 {{ id }}
</div>
<StripeCheckout />
</template>
<style scoped>
 
</style>