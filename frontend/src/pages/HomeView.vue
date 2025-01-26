<script setup lang="ts">
import AboutSection from "@/components/sections/AboutSection.vue";
import CoachList from "../components/trainer/CoachList.vue";
import AbonementsList from "@/components/abonements/AbonementsList.vue";
import HeaderSection from "@/components/sections/HeaderSection.vue";
import SubscribeSection from "@/components/sections/SubscribeSection.vue";
import PoolSection from "@/components/sections/PoolSection.vue";
import WomenSection from "@/components/sections/WomenSection.vue";
</script>

<template>
  <ArrowUpButton />
  <HeaderSection />
  <AboutSection />
  <AbonementsList />
  <WomenSection />
  <CoachList />
  <PoolSection />
  <SubscribeSection />
</template>
