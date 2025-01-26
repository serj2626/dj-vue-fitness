<script setup>
import { faqs } from "@/types/faq";
import {
  FwbAccordion,
  FwbAccordionContent,
  FwbAccordionHeader,
  FwbAccordionPanel,
} from "flowbite-vue";
</script>
<template>
  <section id="faq" class="faq py-6 mb-3">
    <div class="container faq__container">
      <h3 class="faq__title text-3xl text-center text-yellow-300 mb-16">Ответы на часто задаваемые вопросы</h3>
      <fwb-accordion :open-first-item="false">
        <fwb-accordion-panel v-for="faq in faqs" :key="faq.id">
          <fwb-accordion-header>{{ faq.question }}</fwb-accordion-header>
          <fwb-accordion-content>
            <div>
              <p class="mb-2 text-gray-500 dark:text-gray-400">
                {{ faq.answer }}
              </p>
            </div>
          </fwb-accordion-content>
        </fwb-accordion-panel>
      </fwb-accordion>
    </div>
  </section>
</template>
