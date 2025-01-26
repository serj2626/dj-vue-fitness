<script setup lang="ts">
import AboutSection from "@/components/sections/AboutSection.vue";
import CoachList from "../components/sections/CoachListSection.vue";
import AbonementsList from "@/components/sections/AbonementsListSection.vue";
import HeaderSection from "@/components/sections/HeaderSection.vue";
import SubscribeSection from "@/components/sections/SubscribeSection.vue";
import PoolSection from "@/components/sections/PoolSection.vue";
import WomenSection from "@/components/sections/WomenSection.vue";
import FAQSection from "@/components/sections/FAQSection.vue";
</script>

<template>
  <ArrowUpButton />
  <HeaderSection />
  <AboutSection />
  <AbonementsList />
  <WomenSection />
  <CoachList />
  <FAQSection />
  <PoolSection />
  <SubscribeSection />
</template>
