<script setup lang="ts">
import { FwbButton } from "flowbite-vue";

type View = "review" | "abonement" | "training";

defineProps({
  view: {
    type: String as () => View,
    required: true,
  },
});

const emit = defineEmits(["closeModal", "delete"]);
</script>

<template>
  <div @click="$emit('closeModal')" class="modal z-50">
    <div class="modal-content w-2/3 relative">
      <div
        @click.stop
        class="absolute top-[50%] left-[50%] translate-x-[-50%] translate-y-[-50%] bg-white rounded-lg shadow dark:bg-gray-700 p-6"
      >
        <div
          class="flex items-center justify-between p-6 md:p-5 rounded-t dark:border-gray-600"
        >
          <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
            <div v-if="view === 'review'">
              Вы действительно хотите удалить отзыв?
            </div>
            <div v-else-if="view === 'abonement'">
              Вы действительно хотите удалить абонемент?
            </div>
            <div v-else-if="view === 'training'">
              Вы действительно хотите удалить тренировку?
            </div>
          </h3>
        </div>
        <div
          class="flex items-center gap-5 justify-end p-4 md:p-5 border-t border-gray-200 rounded-b \
          dark:border-gray-600"
        >
          <fwb-button size="lg" @click="emit('closeModal')" color="light">
            Отмена
          </fwb-button>
          <fwb-button size="lg" @click="emit('delete')" color="red">
            Удалить
          </fwb-button>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
}
</style>
