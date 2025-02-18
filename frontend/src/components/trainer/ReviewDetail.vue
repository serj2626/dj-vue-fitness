<script setup lang="ts">
import type { IReview } from "@/types/workout";
import { FwbRating } from "flowbite-vue";
import { useUserStore } from "@/stores/auth";
import { ref } from "vue";

defineProps<{
  review: IReview;
}>();

const showModal = ref(false);
const showModalForUpdate = ref(false);

const store = useUserStore();

const emit = defineEmits(["deleteReview"]);

const deleteReview = (id: number) => {
  showModal.value = false;
  emit("deleteReview", id);
};
</script>

<template>
  <Confirm
    v-if="showModal"
    view="review"
    @closeModal="showModal = false"
    @delete="deleteReview(review.id)"
  />

  <UModal
    v-if="showModalForUpdate"
    orderType="updateReview"
    :text="review.text"
    @closeModal="showModalForUpdate = false"
  />

  <div
    class="reviews__desc flex flex-col justify-center gap-6 py-2 px-4 rounded-md my-10"
  >
    <div class="reviews-desc__header flex justify-between items-center">
      <div class="flex items-center gap-3">
        <h3>{{ review.user.username }}</h3>
        <fwb-rating size="sm" :rating="review.rating" />

        <div
          v-if="store.auth.username === review.user.username"
          class="flex items-center gap-2"
        >
          <svg
            @click="showModal = true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="size-5 svg-del"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0"
            />
          </svg>

          <svg
            @click="showModalForUpdate = true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="size-5 svg-edit"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L10.582 16.07a4.5 4.5 0 0 1-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 0 1 1.13-1.897l8.932-8.931Zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0 1 15.75 21H5.25A2.25 2.25 0 0 1 3 18.75V8.25A2.25 2.25 0 0 1 5.25 6H10"
            />
          </svg>
        </div>
      </div>

      <span>{{ review.date_age }} назад</span>
    </div>

    <div class="reviews-desc__body">
      <p class="word-wrap">{{ review.text }}</p>
    </div>
  </div>
</template>

<style scoped lang="scss">
.word-wrap {
  word-wrap: break-word;
}

.reviews__desc {
  background-color: rgba(102, 93, 93, 0.223);
  color: white;
  box-shadow: 0 0 15px rgb(219, 217, 217);
}

svg {
  cursor: pointer;
  transition: all 0.3s ease-in;
}

.svg-del:hover {
  stroke: rgb(248, 74, 74);
}

.svg-edit:hover {
  stroke: rgb(29, 216, 29);
}
</style>
