<script setup lang="ts">
defineProps({
    coach: {
        type: Object,
        required: true
    }
})

console.log("coach", coach);
</script>

<template>
    <div class="card">
        <div class="card__img">
            <img :src="coach.avatar" alt="">
        </div>  
    </div>
</template>


<style scoped>

.card{
    max-height: 400px;
    background-color: #FFF;
    border-radius: 20px;
    box-shadow: 0 0 15px rgb(219, 217, 217);
}

</style>