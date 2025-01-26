<script setup>
import { faqs } from "@/types/faq";
import Accordion from "primevue/accordion";
import AccordionPanel from "primevue/accordionpanel";
import AccordionHeader from "primevue/accordionheader";
import AccordionContent from "primevue/accordioncontent";
</script>
<template>
  <section id="faq" class="card container py-12">
    <h3 class="faq__title text-3xl text-center text-yellow-300 mb-16">
      Ответы на часто задаваемые вопросы
    </h3>
    <Accordion multiple class="w-3/4 mx-auto">
      <AccordionPanel v-for="(faq, index) in faqs" :key="faq.id" :value="index">
        <AccordionHeader
          ><span class="bg-yellow-300 rounded-full py-2 px-4">{{ faq.id }}</span>
          {{ faq.question }}</AccordionHeader
        >
        <AccordionContent>
          <p class="m-0">
            {{ faq.answer }}
          </p>
        </AccordionContent>
      </AccordionPanel>
    </Accordion>
  </section>
</template>
