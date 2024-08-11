<script setup lang="ts">
import MyAbonement from "@/components/profile/MyAbonement.vue";
import MySettings from "@/components/profile/MySettings.vue";
import MyTrainings from "@/components/profile/MyTrainings.vue";

import { useUserStore } from "@/stores/auth";
import { storeToRefs } from "pinia";
import { ref } from "vue";

const store = useUserStore();
const { auth: user } = storeToRefs(store);

const showAction = ref(1);
</script>

<template>
  <div class="container row mt-[150px] overflow-x-hidden">

    <!-- <p class="text-white">{{ user }}</p> -->
    <div class="actions flex justify-center items-center gap-10 mt-10">
      <ProfileButton
        @click="showAction = 1"
        :class="{ action__btn_active: showAction === 1 }"
        title="Настройки"
      />
      <ProfileButton
        @click="showAction = 2"
        :class="{ action__btn_active: showAction === 2 }"
        title="Абонементы"
      />
      <ProfileButton
        @click="showAction = 3"
        :class="{ action__btn_active: showAction === 3 }"
        title="Тренировки"
      />
    </div>

    <div
      class="mt-28"
    >
      <MySettings :user="user" v-if="showAction === 1" />
      <MyAbonement v-if="showAction === 2" />
      <MyTrainings v-if="showAction === 3" />
    </div>
  </div>
</template>

<style scoped>
.profile {
  background: linear-gradient(
    45deg,
    rgb(236, 48, 180) 0%,
    rgb(0, 255, 221) 100%
  );
  box-shadow: 0 0 25px rgb(201, 192, 13);
}

img {
  border-radius: 50%;
  border: 3px solid orange;
  padding: 10px;
}

.action__btn_active {
  background: linear-gradient(
    45deg,
    rgb(162, 54, 187) 0%,
    rgb(221, 255, 2) 100%
  );
}
</style>
