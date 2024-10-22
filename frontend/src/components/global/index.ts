import type { App } from "vue";
import ArrowUpButton from "./ArrowUpButton.vue";
import UModal from "./UModal.vue";
import URating from "./URating.vue";
import USelect from "./USelect.vue";
import UInput from "./UInput.vue";
import UButton from "./UButton.vue";
import AuthCard from "./AuthCard.vue";

const components = [
  { name: "ArrowUpButton", component: ArrowUpButton },
  { name: "UModal", component: UModal },
  { name: "URating", component: URating },
  { name: "USelect", component: USelect },
  { name: "UInput", component: UInput },
  { name: "UButton", component: UButton },
  { name: "AuthCard", component: AuthCard },
];

export default {
  install(app: App) {
    components.forEach(({ name, component }) => {
      app.component(name, component);
    });
  },
};
