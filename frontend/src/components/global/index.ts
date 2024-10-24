import type { App } from "vue";
import ArrowUpButton from "./ArrowUpButton.vue";
import URating from "./URating.vue";
import UButton from "./UButton.vue";
import AuthCard from "./AuthCard.vue";
import CreateOrderModal from "./CreateOrderModal.vue";

const components = [
  { name: "ArrowUpButton", component: ArrowUpButton },
  { name: "URating", component: URating },
  { name: "UButton", component: UButton },
  { name: "AuthCard", component: AuthCard },
  { name: "CreateOrderModal", component: CreateOrderModal },
];

export default {
  install(app: App) {
    components.forEach(({ name, component }) => {
      app.component(name, component);
    });
  },
};
