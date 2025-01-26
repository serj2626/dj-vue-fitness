<script setup lang="ts">
import AboutSection from "@/components/sections/AboutSection.vue";
import CoachList from "../components/sections/CoachList.vue";
import AbonementsList from "@/components/sections/AbonementsList.vue";
import HeaderSection from "@/components/sections/HeaderSection.vue";
import SubscribeSection from "@/components/sections/SubscribeSection.vue";
import PoolSection from "@/components/sections/PoolSection.vue";
import WomenSection from "@/components/sections/WomenSection.vue";
import FAQ from "@/components/sections/FAQ.vue";
</script>

<template>
  <ArrowUpButton />
  <HeaderSection />
  <AboutSection />
  <AbonementsList />
  <WomenSection />
  <CoachList />
  <FAQ />
  <PoolSection />
  <SubscribeSection />
</template>
