<script setup lang="ts">
import { ref, onMounted } from "vue";
import type { ITrainerImage } from "@/types/workout";
import Button from "primevue/button"; // moved import statement above the cursor
import Galleria from "primevue/galleria";

defineProps<{
  images: ITrainerImage[]; // added semicolon at the end of the line
}>();
const displayBasic = ref(false);

const responsiveOptions = ref([
  {
    breakpoint: "1500px",
    numVisible: 5,
  },
  {
    breakpoint: "1024px",
    numVisible: 3,
  },
  {
    breakpoint: "768px",
    numVisible: 2,
  },
  {
    breakpoint: "560px",
    numVisible: 1,
  },
]);
</script>
<template>
  <!-- <div class="bg-rose-500">
{{ images }}
  </div> -->
  <div class="card flex justify-center">
    <Galleria
      v-model:visible="displayBasic"
      images="images"
      :responsiveOptions="responsiveOptions"
      :numVisible="9"
      containerStyle="max-width: 50%"
      :circular="true"
      :fullScreen="true"
      :showItemNavigators="true"
    >
      <template #item="slotProps">
        {{ slotProps }}
        <img :src="slotProps.item.image" style="width: 100%; display: block" />
      </template>
      <!-- <template #thumbnail="slotProps">
        <img :src="slotProps.item.image" style="display: block" />
      </template> -->
    </Galleria>

    <Button
      label="Show"
      icon="pi pi-external-link"
      @click="displayBasic = true"
      class="bg-rose-300"
    />
  </div>
</template>
